#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
import shutil
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


FOLO_CATEGORY_DEFAULT = "AI FrontEnd"
JUYA_RSS_URL_DEFAULT = "https://imjuya.github.io/juya-ai-daily/rss.xml"
PAPER_FEED_TITLE = "cs.AI updates on arXiv.org"
ALLOWED_ARXIV_CATEGORIES = {"cs.LG", "cs.CL", "cs.SE"}
BLACKLIST_TERMS = [
    "clinical",
    "psychiatric",
    "lung cancer",
    "biomechanical",
    "traffic",
    "driving",
    "emboli",
    "field medicine",
    "legal",
    "graph",
]
JUYA_CATEGORIES = {
    "要闻",
    "模型发布",
    "开发生态",
    "产品应用",
    "技术与洞察",
    "行业动态",
    "前瞻与传闻",
}
SCORE_THRESHOLD = 60
SCORE_KEYS = [
    "application_relevance",
    "new_signal",
    "engineering_utility",
    "timeliness_rarity",
]


@dataclass
class TimelineEntry:
    title: str
    url: str
    published_at: str
    description: str
    summary: str
    categories: List[str]
    feed_title: str
    feed_url: str
    feed_site_url: str
    raw: Dict[str, Any]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the Daily AI Info digest dataset.")
    parser.add_argument("--category", default=FOLO_CATEGORY_DEFAULT)
    parser.add_argument("--hours", type=int, default=24)
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--limit", type=int, default=100)
    parser.add_argument("--juya-rss-url", default=JUYA_RSS_URL_DEFAULT)
    parser.add_argument("--paper-source", choices=["auto", "folo", "arxiv"], default="auto")
    parser.add_argument("--folo-timeout", type=int, default=45)
    parser.add_argument("--arxiv-max-results", type=int, default=80)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--state-file", default="data/paper-state.json")
    parser.add_argument("--run-log", default="data/run-log.jsonl")
    parser.add_argument("--run-id")
    return parser.parse_args()


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return utc_now().isoformat()


def read_url_text(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "PersonalAIDailyReport/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError:
        # Some local Python installs miss CA certificates. Retry without changing
        # system trust so the build remains diagnosable and self-contained.
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(req, timeout=timeout, context=context) as response:
            return response.read().decode("utf-8")


def clean_html(value: str) -> str:
    value = re.sub(r"<script[^>]*>.*?</script>", " ", value, flags=re.S | re.I)
    value = re.sub(r"<style[^>]*>.*?</style>", " ", value, flags=re.S | re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(unescape(value).split())


def first_href(value: str) -> Optional[str]:
    match = re.search(r'<a[^>]+href="([^"]+)"', value)
    return match.group(1) if match else None


def parse_rss_date(value: str) -> str:
    try:
        return parsedate_to_datetime(value).astimezone(timezone.utc).isoformat()
    except Exception:
        return value


def parse_juya_news(rss_url: str) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    xml_text = read_url_text(rss_url)
    root = ET.fromstring(xml_text)
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError("Juya RSS channel not found")
    item = channel.find("item")
    if item is None:
        raise RuntimeError("Juya RSS has no item")

    content = item.findtext("{http://purl.org/rss/1.0/modules/content/}encoded") or ""
    issue = {
        "feed_title": channel.findtext("title") or "",
        "feed_link": channel.findtext("link") or "",
        "feed_description": channel.findtext("description") or "",
        "last_build_date": parse_rss_date(channel.findtext("lastBuildDate") or ""),
        "issue_title": item.findtext("title") or "",
        "issue_url": item.findtext("link") or "",
        "issue_guid": item.findtext("guid") or "",
        "published_at": parse_rss_date(item.findtext("pubDate") or ""),
        "rss_url": rss_url,
    }

    overview = content.split("<hr>", 1)[0]
    category_by_title: Dict[str, str] = {}
    parts = re.split(r"<h3[^>]*>(.*?)</h3>", overview, flags=re.S | re.I)
    for index in range(1, len(parts), 2):
        category = clean_html(parts[index])
        if category not in JUYA_CATEGORIES:
            continue
        for li_html in re.findall(r"<li[^>]*>(.*?)</li>", parts[index + 1], flags=re.S | re.I):
            title = clean_html(li_html)
            title = re.sub(r"↗\s*#\d+$", "", title).strip()
            title = re.sub(r"\s+#\d+$", "", title).strip()
            if title:
                category_by_title[title] = category

    h2_matches = list(re.finditer(r"<h2[^>]*>(.*?)</h2>", content, flags=re.S | re.I))
    news: List[Dict[str, Any]] = []
    for idx, match in enumerate(h2_matches):
        title_html = match.group(1)
        title = clean_html(title_html)
        if title == "概览":
            continue
        link = first_href(title_html)
        if not link:
            continue
        title = re.sub(r"\s+#\d+$", "", title).strip()
        end = h2_matches[idx + 1].start() if idx + 1 < len(h2_matches) else len(content)
        body = content[match.end() : end]
        summary_parts: List[str] = []
        for tag in ["blockquote", "p"]:
            blocks = re.findall(fr"<{tag}[^>]*>(.*?)</{tag}>", body, flags=re.S | re.I)
            for block in blocks:
                text = clean_html(block)
                if not text or text == "相关链接：" or text.startswith("http"):
                    continue
                if len(text) > 8:
                    summary_parts.append(text)
            if summary_parts:
                break
        summary = " ".join(summary_parts[:2]).strip()
        news.append(
            {
                "title": title,
                "url": link,
                "published_at": issue["published_at"],
                "description": summary,
                "summary": summary,
                "category": category_by_title.get(title, "未分类"),
                "source": "juya",
                "issue_title": issue["issue_title"],
                "issue_url": issue["issue_url"],
            }
        )

    return news, issue


def run_json_command(args: List[str], timeout: int) -> Dict[str, Any]:
    last_error = ""
    for attempt in range(2):
        try:
            proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", timeout=timeout)
        except subprocess.TimeoutExpired as exc:
            raise TimeoutError(f"Command timed out after {timeout}s: {' '.join(args)}") from exc
        if proc.returncode == 0:
            try:
                return json.loads(proc.stdout)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"Failed to parse JSON from command: {' '.join(args)}\n{proc.stdout}") from exc
        last_error = proc.stderr or proc.stdout
        if "aborted" not in last_error.lower() or attempt == 1:
            break
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Command failed: {' '.join(args)}\n{last_error}")


def resolve_executable(name: str) -> str:
    candidates = [name]
    if sys.platform.startswith("win"):
        candidates = [f"{name}.cmd", f"{name}.exe", name]
    for candidate in candidates:
        path = shutil.which(candidate)
        if path:
            return path
    raise RuntimeError(f"Could not find executable for {name}")


def parse_dt(value: str) -> datetime:
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    return datetime.fromisoformat(value)


def fetch_timeline(category: str, hours: int, limit: int, timeout: int) -> List[TimelineEntry]:
    cutoff = utc_now() - timedelta(hours=hours)
    cursor: Optional[str] = None
    collected: List[TimelineEntry] = []

    while True:
        cmd = [
            resolve_executable("npx"),
            "--yes",
            "folocli@latest",
            "timeline",
            "--category",
            category,
            "--limit",
            str(limit),
            "--format",
            "json",
        ]
        if cursor:
            cmd.extend(["--cursor", cursor])

        payload = run_json_command(cmd, timeout=timeout)
        data = payload.get("data") or {}
        entries = data.get("entries") or []
        if not entries:
            break

        stop = False
        for item in entries:
            entry = item.get("entries") or {}
            published_at = entry.get("publishedAt")
            if not published_at:
                continue
            published_dt = parse_dt(published_at)
            if published_dt < cutoff:
                stop = True
                continue
            collected.append(
                TimelineEntry(
                    title=entry.get("title") or "",
                    url=entry.get("url") or "",
                    published_at=published_at,
                    description=entry.get("description") or "",
                    summary=entry.get("summary") or "",
                    categories=list(entry.get("categories") or []),
                    feed_title=((item.get("feeds") or {}).get("title") or ""),
                    feed_url=((item.get("feeds") or {}).get("url") or ""),
                    feed_site_url=((item.get("feeds") or {}).get("siteUrl") or ""),
                    raw=item,
                )
            )

        cursor = data.get("nextCursor")
        if stop or not data.get("hasNext") or not cursor:
            break
        time.sleep(0.2)

    return collected


def is_blacklisted(text: str) -> bool:
    lowered = text.lower()
    return any(term in lowered for term in BLACKLIST_TERMS)


def normalize_arxiv_id(value: str) -> str:
    value = value.strip()
    value = re.sub(r"v\d+$", "", value)
    return value


def extract_arxiv_id(url: str) -> Optional[str]:
    match = re.search(r"arxiv\.org/abs/([^/?#]+)", url)
    return normalize_arxiv_id(match.group(1)) if match else None


def row_from_arxiv_entry(entry: ET.Element, namespace: Dict[str, str]) -> Dict[str, Any]:
    entry_id = entry.findtext("atom:id", default="", namespaces=namespace).replace("http://", "https://")
    arxiv_id = normalize_arxiv_id(entry_id.rsplit("/", 1)[-1])
    title = " ".join(entry.findtext("atom:title", default="", namespaces=namespace).split())
    abstract = " ".join(entry.findtext("atom:summary", default="", namespaces=namespace).split())
    categories = [node.attrib.get("term", "") for node in entry.findall("atom:category", namespace)]
    published_at = entry.findtext("atom:published", default="", namespaces=namespace)
    return {
        "id": f"arxiv:{arxiv_id}",
        "arxiv_id": arxiv_id,
        "title": title,
        "url": f"https://arxiv.org/abs/{arxiv_id}",
        "published_at": published_at,
        "publish_date": published_at[:10],
        "description": abstract,
        "summary": abstract,
        "abstract": abstract,
        "categories": categories,
        "api_categories": categories,
        "feed_title": PAPER_FEED_TITLE,
        "source": "arxiv_api",
    }


def fetch_arxiv_latest(max_results: int) -> List[Dict[str, Any]]:
    search = "cat:cs.AI OR cat:cs.CL OR cat:cs.LG OR cat:cs.SE"
    query = urllib.parse.urlencode(
        {
            "search_query": search,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "start": "0",
            "max_results": str(max_results),
        }
    )
    xml_text = read_url_text(f"https://export.arxiv.org/api/query?{query}", timeout=45)
    root = ET.fromstring(xml_text)
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    return [row_from_arxiv_entry(entry, namespace) for entry in root.findall("atom:entry", namespace)]


def fetch_arxiv_rss_latest(max_results: int) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for category in ["cs.AI", "cs.CL", "cs.LG", "cs.SE"]:
        xml_text = read_url_text(f"https://rss.arxiv.org/rss/{category}", timeout=30)
        root = ET.fromstring(xml_text)
        channel = root.find("channel")
        if channel is None:
            continue
        for item in channel.findall("item"):
            link = item.findtext("link") or ""
            arxiv_id = extract_arxiv_id(link) or link.rsplit("/", 1)[-1]
            if not arxiv_id or arxiv_id in seen:
                continue
            seen.add(arxiv_id)
            description = clean_html(item.findtext("description") or "")
            abstract = description
            marker = "Abstract:"
            if marker in description:
                abstract = description.split(marker, 1)[1].strip()
            categories = [node.text or "" for node in item.findall("category")]
            pub_date = parse_rss_date(item.findtext("pubDate") or "")
            rows.append(
                {
                    "id": f"arxiv:{normalize_arxiv_id(arxiv_id)}",
                    "arxiv_id": normalize_arxiv_id(arxiv_id),
                    "title": clean_html(item.findtext("title") or ""),
                    "url": f"https://arxiv.org/abs/{normalize_arxiv_id(arxiv_id)}",
                    "published_at": pub_date,
                    "publish_date": pub_date[:10],
                    "description": abstract,
                    "summary": abstract,
                    "abstract": abstract,
                    "categories": categories,
                    "api_categories": categories,
                    "feed_title": PAPER_FEED_TITLE,
                    "source": "arxiv_rss",
                }
            )
            if len(rows) >= max_results:
                return rows
    return rows


def fetch_arxiv_abstracts(arxiv_ids: Iterable[str]) -> Dict[str, Dict[str, Any]]:
    ids = [normalize_arxiv_id(x) for x in arxiv_ids if x]
    if not ids:
        return {}

    output: Dict[str, Dict[str, Any]] = {}
    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    for i in range(0, len(ids), 10):
        chunk = ids[i : i + 10]
        query = urllib.parse.urlencode({"id_list": ",".join(chunk)})
        xml_text = read_url_text(f"https://export.arxiv.org/api/query?{query}", timeout=30)
        root = ET.fromstring(xml_text)
        for entry in root.findall("atom:entry", namespace):
            row = row_from_arxiv_entry(entry, namespace)
            output[row["arxiv_id"]] = row
        time.sleep(0.2)
    return output


def paper_rows_from_folo(entries: List[TimelineEntry]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    raw: List[Dict[str, Any]] = []
    dropped: List[Dict[str, Any]] = []
    kept: List[Dict[str, Any]] = []
    for item in entries:
        if item.feed_title != PAPER_FEED_TITLE:
            continue
        row = {
            "title": item.title,
            "url": item.url,
            "published_at": item.published_at,
            "publish_date": item.published_at[:10],
            "description": item.description,
            "summary": item.summary,
            "categories": item.categories,
            "feed_title": item.feed_title,
            "source": "folo",
        }
        raw.append(row)
        result = filter_paper_row(row)
        if result:
            dropped.append(result)
            continue
        row["arxiv_id"] = extract_arxiv_id(item.url) or ""
        row["id"] = f"arxiv:{row['arxiv_id']}" if row["arxiv_id"] else item.url
        kept.append(row)

    abstracts = fetch_arxiv_abstracts([row.get("arxiv_id") for row in kept if row.get("arxiv_id")])
    for row in kept:
        abstract_data = abstracts.get(row.get("arxiv_id") or "", {})
        row["abstract"] = abstract_data.get("abstract") or row.get("summary") or row.get("description") or ""
        row["api_categories"] = abstract_data.get("api_categories") or abstract_data.get("categories") or row["categories"]
    return kept, dropped


def filter_paper_row(row: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    text_blob = " ".join([row.get("title", ""), row.get("description", ""), row.get("summary", ""), row.get("abstract", "")])
    if is_blacklisted(text_blob):
        clone = dict(row)
        clone["drop_reason"] = "blacklist"
        return clone
    categories = set(row.get("api_categories") or row.get("categories") or [])
    if not categories.intersection(ALLOWED_ARXIV_CATEGORIES):
        clone = dict(row)
        clone["drop_reason"] = "category"
        return clone
    return None


def filter_arxiv_rows(rows: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    kept: List[Dict[str, Any]] = []
    dropped: List[Dict[str, Any]] = []
    for row in rows:
        result = filter_paper_row(row)
        if result:
            dropped.append(result)
        else:
            kept.append(row)
    return kept, dropped


def keyword_score(text: str, groups: List[List[str]], base: int = 4) -> int:
    lowered = text.lower()
    score = base
    for group in groups:
        if any(term in lowered for term in group):
            score += 5
    return min(score, 25)


def score_paper(row: Dict[str, Any]) -> Dict[str, Any]:
    text = " ".join([row.get("title", ""), row.get("abstract", "")])
    app = keyword_score(
        text,
        [
            ["agent", "workflow", "tool", "retrieval", "rag"],
            ["coding", "software", "developer", "program"],
            ["document", "ocr", "gui", "interface", "browser"],
            ["judge", "evaluation", "benchmark", "safety"],
        ],
        base=5,
    )
    new_signal = keyword_score(
        text,
        [
            ["introduce", "propose", "new benchmark", "benchmark"],
            ["agentic", "multi-agent", "planner", "executor"],
            ["dataset", "framework", "protocol"],
            ["real-world", "repository", "deployed", "workflow"],
        ],
        base=5,
    )
    engineering = keyword_score(
        text,
        [
            ["code", "repository", "software", "test", "execution"],
            ["tool", "api", "workflow", "framework", "system"],
            ["retrieval", "reranker", "fuzz", "static analysis"],
            ["available", "github", "benchmark", "evaluation"],
        ],
        base=4,
    )
    timeliness = keyword_score(
        text,
        [
            ["agent", "coding agent", "agentic"],
            ["retrieval", "rag", "long context", "memory"],
            ["judge", "hallucination", "safety"],
            ["multimodal", "document", "ocr"],
        ],
        base=4,
    )
    detail = {
        "application_relevance": app,
        "new_signal": new_signal,
        "engineering_utility": engineering,
        "timeliness_rarity": timeliness,
    }
    total = sum(detail.values())
    scored = dict(row)
    scored["score_detail"] = detail
    scored["score_total"] = total
    scored["score_reason"] = build_score_reason(scored)
    scored["one_sentence_summary"] = build_one_sentence_summary(scored)
    return scored


def build_score_reason(row: Dict[str, Any]) -> str:
    title = row.get("title", "")
    abstract = row.get("abstract", "").lower()
    reasons: List[str] = []
    if "agent" in abstract or "agent" in title.lower():
        reasons.append("agent relevance")
    if any(term in abstract for term in ["benchmark", "evaluation", "dataset"]):
        reasons.append("evaluation signal")
    if any(term in abstract for term in ["code", "software", "test", "retrieval", "workflow"]):
        reasons.append("engineering utility")
    return ", ".join(reasons) or "matches paper filter and scoring threshold"


def build_one_sentence_summary(row: Dict[str, Any]) -> str:
    title = row.get("title", "")
    abstract = row.get("abstract", "")
    lowered = (title + " " + abstract).lower()
    if "coding agent" in lowered or "software" in lowered:
        focus = "软件工程或 coding agent"
    elif "retriev" in lowered or "rag" in lowered:
        focus = "检索增强和 agentic search"
    elif "judge" in lowered or "instruction following" in lowered:
        focus = "模型评测与 judge 能力"
    elif "ocr" in lowered or "document" in lowered:
        focus = "真实文档处理和多模态理解"
    elif "planner" in lowered or "reasoning" in lowered:
        focus = "推理规划和执行反馈"
    elif "safety" in lowered or "vulnerability" in lowered:
        focus = "AI 安全和漏洞验证"
    else:
        focus = "AI 系统能力改进"
    return f"这篇论文围绕「{title}」展开，重点提供了面向{focus}的新方法、评测或工程线索。"


def load_paper_state(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"version": 1, "updated_at": None, "papers": []}
    return json.loads(path.read_text(encoding="utf-8"))


def save_paper_state(path: Path, state: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def update_paper_state(state_path: Path, candidates: List[Dict[str, Any]], top_k: int, run_id: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    state = load_paper_state(state_path)
    papers = state.setdefault("papers", [])
    existing = {paper.get("id"): paper for paper in papers}
    added = 0
    skipped_low_score = 0
    now = iso_now()

    for candidate in candidates:
        scored = score_paper(candidate)
        if scored["score_total"] < SCORE_THRESHOLD:
            skipped_low_score += 1
            continue
        paper_id = scored.get("id") or scored.get("url")
        if paper_id in existing:
            current = existing[paper_id]
            if current.get("if_pushed", 0) == 0 and scored["score_total"] > current.get("score_total", 0):
                current.update({k: v for k, v in scored.items() if k not in {"if_pushed", "added_at", "pushed_at", "pushed_run_id"}})
            continue
        scored["if_pushed"] = 0
        scored["added_at"] = now
        scored["pushed_at"] = None
        scored["source_run_id"] = run_id
        scored["pushed_run_id"] = None
        papers.append(scored)
        existing[paper_id] = scored
        added += 1

    available = [paper for paper in papers if paper.get("if_pushed", 0) == 0]
    available.sort(key=lambda paper: (paper.get("score_total", 0), paper.get("publish_date", "")), reverse=True)
    selected = available[:top_k]
    for paper in selected:
        paper["if_pushed"] = 1
        paper["pushed_at"] = now
        paper["pushed_run_id"] = run_id

    state["updated_at"] = now
    save_paper_state(state_path, state)

    status = {
        "state_file": str(state_path),
        "new_candidate_count": len(candidates),
        "added_to_state_count": added,
        "skipped_low_score_count": skipped_low_score,
        "selected_count": len(selected),
        "waiting_remaining_count": len([paper for paper in papers if paper.get("if_pushed", 0) == 0]),
        "selected_ids": [paper.get("id") for paper in selected],
    }
    return selected, status


def fetch_paper_candidates(args: argparse.Namespace, logs: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], str]:
    if args.paper_source in {"auto", "folo"}:
        try:
            entries = fetch_timeline(args.category, args.hours, args.limit, args.folo_timeout)
            kept, dropped = paper_rows_from_folo(entries)
            logs.append({"stage": "paper_fetch", "source": "folo", "status": "ok", "entries": len(entries), "kept": len(kept)})
            if kept or args.paper_source == "folo":
                return kept, dropped, "folo"
        except Exception as exc:
            logs.append({"stage": "paper_fetch", "source": "folo", "status": "failed", "error": str(exc)})
            if args.paper_source == "folo":
                raise

    try:
        arxiv_rows = fetch_arxiv_latest(args.arxiv_max_results)
        arxiv_source = "arxiv_api"
    except Exception as exc:
        logs.append({"stage": "paper_fetch", "source": "arxiv_api", "status": "failed", "error": str(exc)})
        arxiv_rows = fetch_arxiv_rss_latest(args.arxiv_max_results)
        arxiv_source = "arxiv_rss"
    kept, dropped = filter_arxiv_rows(arxiv_rows)
    logs.append({"stage": "paper_fetch", "source": arxiv_source, "status": "ok", "raw": len(arxiv_rows), "kept": len(kept)})
    return kept, dropped, arxiv_source


def build_scaffold_markdown(data: Dict[str, Any]) -> str:
    lines = ["# Daily AI Info", "", "## News", ""]
    current_category = None
    for idx, item in enumerate(data["news"], start=1):
        category = item.get("category") or "未分类"
        if category != current_category:
            current_category = category
            lines.extend([f"### {category}", ""])
        lines.extend(
            [
                f"{idx}. **{item['title']}**",
                "",
                "**Original Content in Chinese:**",
                item.get("summary") or item.get("description") or "",
                "",
                "**Original Link:**",
                item["url"],
                "",
            ]
        )

    lines.extend(["", "## Paper", ""])
    if not data["selected_papers"]:
        lines.extend(["今日未检索到可推送的 paper。", ""])
    for idx, item in enumerate(data["selected_papers"], start=1):
        lines.extend(
            [
                f"{idx}. **{item['title']}**",
                "",
                "**Publish Date:**",
                item.get("publish_date") or "",
                "",
                "**一句话总结:**",
                item.get("one_sentence_summary") or "",
                "",
                "**Link:**",
                item["url"],
                "",
            ]
        )
    return "\n".join(lines)


def append_run_log(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    run_id = args.run_id or utc_now().astimezone().date().isoformat()
    logs: List[Dict[str, Any]] = []

    news, juya_issue = parse_juya_news(args.juya_rss_url)
    logs.append({"stage": "news_fetch", "source": "juya", "status": "ok", "news_count": len(news), "issue": juya_issue})

    paper_candidates, paper_dropped, paper_source = fetch_paper_candidates(args, logs)
    selected_papers, paper_status = update_paper_state(Path(args.state_file), paper_candidates, args.top_k, run_id)
    paper_status["source"] = paper_source

    dataset = {
        "generated_at": iso_now(),
        "run_id": run_id,
        "juya_issue": juya_issue,
        "stats": {
            "news_count": len(news),
            "paper_candidate_count": len(paper_candidates),
            "paper_dropped_count": len(paper_dropped),
            "paper_selected_count": len(selected_papers),
        },
        "rules": {
            "allowed_categories": sorted(ALLOWED_ARXIV_CATEGORIES),
            "blacklist_terms": BLACKLIST_TERMS,
            "score_keys": SCORE_KEYS,
            "score_threshold": SCORE_THRESHOLD,
        },
        "news": news,
        "paper_candidates": paper_candidates,
        "paper_dropped": paper_dropped,
        "selected_papers": selected_papers,
        "paper_status": paper_status,
        "logs": logs,
    }
    scaffold = build_scaffold_markdown(dataset)

    json_path = output_dir / "digest-data.json"
    md_path = output_dir / "digest-scaffold.md"
    json_path.write_text(json.dumps(dataset, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(scaffold, encoding="utf-8")

    run_log = {
        "run_id": run_id,
        "generated_at": dataset["generated_at"],
        "juya_issue_title": juya_issue.get("issue_title"),
        "juya_issue_url": juya_issue.get("issue_url"),
        "news_count": len(news),
        "paper_source": paper_source,
        "paper_candidate_count": len(paper_candidates),
        "paper_selected_count": len(selected_papers),
        "paper_added_to_state_count": paper_status["added_to_state_count"],
        "paper_waiting_remaining_count": paper_status["waiting_remaining_count"],
        "logs": logs,
    }
    append_run_log(Path(args.run_log), run_log)

    print(
        json.dumps(
            {
                "json": str(json_path),
                "markdown": str(md_path),
                "state_file": args.state_file,
                "run_log": args.run_log,
                "stats": dataset["stats"],
                "paper_status": paper_status,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
