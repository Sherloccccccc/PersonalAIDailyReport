#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
import urllib.request
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send digest markdown to Feishu/Lark.")
    parser.add_argument("--markdown-file", required=True)
    parser.add_argument("--chat-id")
    parser.add_argument("--user-id")
    parser.add_argument("--delivery-log", help="Optional run-log.json to update with delivery status.")
    parser.add_argument("--result-json", help="Optional path to write raw delivery result JSON.")
    return parser.parse_args()


def resolve_executable(name: str) -> str:
    candidates = [name]
    if sys.platform.startswith("win"):
        candidates = [f"{name}.cmd", f"{name}.exe", name]
    for candidate in candidates:
        path = shutil.which(candidate)
        if path:
            return path
    raise RuntimeError(f"Could not find executable for {name}")


def run_json(args: list[str]) -> dict:
    proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout)
    return json.loads(proc.stdout)


def load_lark_app_credentials() -> tuple[str, str]:
    env_app_id = os.environ.get("LARK_APP_ID") or os.environ.get("FEISHU_APP_ID")
    env_app_secret = os.environ.get("LARK_APP_SECRET") or os.environ.get("FEISHU_APP_SECRET")
    if env_app_id and env_app_secret:
        return env_app_id, env_app_secret

    config_path = Path.home() / ".lark-cli" / "config.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    app = config["apps"][0]
    app_id = app["appId"]
    secret_path = Path.home() / ".lark-cli" / f"appsecret-{app_id}.txt"
    app_secret = secret_path.read_text(encoding="utf-8").strip()
    return app_id, app_secret


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def resolve_self_open_id() -> str:
    cli = resolve_executable("lark-cli")
    payload = run_json([cli, "contact", "+get-user", "--format", "json"])
    return payload["data"]["user"]["open_id"]


def fetch_tenant_access_token() -> str:
    app_id, app_secret = load_lark_app_credentials()
    payload = {"app_id": app_id, "app_secret": app_secret}
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal",
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("code") != 0:
        raise RuntimeError(f"Failed to fetch tenant access token: {result}")
    return result["tenant_access_token"]


def chunk_blocks(blocks: list[str], limit: int = 5000) -> list[list[str]]:
    chunks: list[list[str]] = []
    current: list[str] = []
    size = 0
    for block in blocks:
        block_size = len(block) + 8
        if current and size + block_size > limit:
            chunks.append(current)
            current = []
            size = 0
        current.append(block)
        size += block_size
    if current:
        chunks.append(current)
    return chunks


def markdown_to_blocks(markdown: str) -> tuple[str, list[str]]:
    lines = markdown.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if not lines:
        return "Daily AI Info", []

    title = lines[0].lstrip("\ufeff").strip() or "Daily AI Info"
    body = "\n".join(lines[1:]).strip()
    raw_blocks = [block.strip() for block in body.split("\n\n") if block.strip()]
    return title, raw_blocks


def build_card(title: str, blocks: list[str]) -> dict:
    elements = []
    for i, block in enumerate(blocks):
        elements.append({"tag": "div", "text": {"tag": "lark_md", "content": block}})
        if i != len(blocks) - 1:
            elements.append({"tag": "hr"})
    return {
        "header": {"title": {"tag": "plain_text", "content": title}},
        "elements": elements,
    }


def send_message(token: str, target_field: str, target_value: str, card: dict) -> dict:
    payload = {
        "receive_id": target_value,
        "msg_type": "interactive",
        "content": json.dumps(card, ensure_ascii=False),
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type={target_field}",
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    if result.get("code") != 0:
        raise RuntimeError(f"Failed to send message: {result}")
    return result


def extract_message_id(result: dict) -> str | None:
    data = result.get("data") or {}
    return data.get("message_id") or data.get("messageId")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def update_delivery_log(path: Path, delivery: dict) -> None:
    if path.exists():
        payload = json.loads(path.read_text(encoding="utf-8"))
    else:
        payload = {}
    payload["delivery"] = delivery
    payload["status"] = delivery.get("status")
    payload["sent_at"] = delivery.get("sent_at")
    write_json(path, payload)


def main() -> int:
    args = parse_args()
    if not args.chat_id and not args.user_id:
        args.user_id = resolve_self_open_id()

    markdown = Path(args.markdown_file).read_text(encoding="utf-8")
    title, blocks = markdown_to_blocks(markdown)
    token = fetch_tenant_access_token()
    target_field = "chat_id" if args.chat_id else "open_id"
    target_value = args.chat_id or args.user_id

    chunked = chunk_blocks(blocks)
    total = len(chunked)
    results = []
    delivery = {
        "channel": "feishu",
        "status": "success",
        "sent_at": utc_now(),
        "target_type": target_field,
        "target_configured": bool(target_value),
        "message_ids": [],
        "parts": total,
    }
    try:
        for index, chunk in enumerate(chunked, start=1):
            part_title = title if total == 1 else f"{title} ({index}/{total})"
            card = build_card(part_title, chunk)
            result = send_message(token, target_field, target_value, card)
            results.append(result)
            message_id = extract_message_id(result)
            if message_id:
                delivery["message_ids"].append(message_id)
    except Exception as exc:
        delivery["status"] = "failed"
        delivery["error"] = str(exc)
        delivery["sent_at"] = utc_now()
        if args.delivery_log:
            update_delivery_log(Path(args.delivery_log), delivery)
        if args.result_json:
            write_json(Path(args.result_json), {"delivery": delivery, "results": results})
        raise

    output = {"delivery": delivery, "results": results}
    if args.delivery_log:
        update_delivery_log(Path(args.delivery_log), delivery)
    if args.result_json:
        write_json(Path(args.result_json), output)

    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
