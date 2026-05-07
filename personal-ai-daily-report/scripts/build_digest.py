#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the Daily AI Info digest dataset.")
    parser.add_argument("--output-dir", default="output")
    parser.add_argument("--juya-rss-url", default=JUYA_RSS_URL_DEFAULT)
    parser.add_argument("--arxiv-max-results", type=int, default=80)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--state-file", default="data/paper-state.json")
    parser.add_argument("--run-log", default=None, help="Optional legacy JSONL run log path.")
    parser.add_argument("--run-summary", default=None, help="Daily run summary JSON path.")
    parser.add_argument("--index-log", default=None, help="Append one JSONL index row for this run.")
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
    specific = build_specific_summary(title, abstract, lowered)
    if specific:
        return specific
    structured = build_structured_chinese_summary(title, abstract, lowered)
    if structured:
        return structured
    return f"这篇论文讨论《{title}》，但摘要里缺少足够明确的方法、数据或评测信息，暂时只能判断它与当前 AI paper 主题相关。"


def build_structured_chinese_summary(title: str, abstract: str, lowered: str) -> str:
    subject = infer_paper_subject(title, lowered)
    method = infer_paper_method(lowered)
    evaluation = infer_paper_evaluation(abstract, lowered)
    usage = infer_paper_usage(lowered)

    parts = [f"这篇论文{method}{subject}"]
    if evaluation:
        parts.append(evaluation)
    if usage:
        parts.append(usage)
    return "；".join(parts) + "。"


def infer_paper_subject(title: str, lowered: str) -> str:
    if "coding agent" in lowered or "software engineering" in lowered:
        return "面向 coding agent 或软件工程任务"
    if "preference" in lowered or "alignment" in lowered:
        return "面向偏好学习、模型对齐或社会价值评测"
    if "retrieval" in lowered or "rag" in lowered:
        return "面向检索增强生成或复杂信息检索任务"
    if "benchmark" in lowered or "evaluation" in lowered:
        return "面向大模型能力评测"
    if "memory" in lowered or "long-context" in lowered or "long context" in lowered:
        return "面向长上下文或 agent 记忆管理"
    if "gui" in lowered or "interface" in lowered or "multimodal" in lowered:
        return "面向多模态界面理解与操作"
    clean_title = title.strip().rstrip(".")
    return f"针对《{clean_title}》这个问题"


def infer_paper_method(lowered: str) -> str:
    if "convert" in lowered and "pairwise preference" in lowered:
        return "提出一个把原始评测数据转换成两两偏好数据的框架，"
    if "benchmark" in lowered:
        return "构建一个新的 benchmark，"
    if "dataset" in lowered:
        return "整理一个新的数据集或任务集合，"
    if "framework" in lowered:
        return "提出一个可复用框架，"
    if "agent" in lowered and ("workflow" in lowered or "tool" in lowered):
        return "设计一套 agent workflow，"
    if "train" in lowered or "fine-tun" in lowered:
        return "训练或微调模型，"
    if "detect" in lowered or "detection" in lowered:
        return "设计检测方法，"
    return "提出一种方法，"


def infer_paper_evaluation(abstract: str, lowered: str) -> str:
    facts = extract_numeric_facts(abstract)
    if "gold label" in lowered and "directional bias" in lowered:
        base = "有标准答案时用 gold label 构造偏好，没有标准答案时用方向性偏差指标补齐监督信号"
    elif "experiment" in lowered or "evaluate" in lowered or "benchmark" in lowered:
        base = "通过实验或基准测试验证方法是否真的改善任务表现"
    elif "dataset" in lowered:
        base = "重点说明数据构造、样本筛选和任务定义方式"
    else:
        base = ""
    if facts:
        return f"{base}，并覆盖{facts}" if base else f"覆盖{facts}"
    return base


def infer_paper_usage(lowered: str) -> str:
    if "preference" in lowered or "alignment" in lowered:
        return "用途是把社会评价任务接入偏好学习、reward model 或模型对齐评测流程"
    if "coding agent" in lowered:
        return "用途是发现 coding agent 在真实开发流程中的能力边界或安全风险"
    if "retrieval" in lowered or "rag" in lowered:
        return "用途是判断检索系统能否为复杂推理持续提供有效证据"
    if "benchmark" in lowered or "evaluation" in lowered:
        return "用途是给模型、agent 或工具链提供更可复现的横向比较标准"
    if "memory" in lowered:
        return "用途是降低长任务执行中的上下文成本，并提升历史信息复用效率"
    return ""


def build_specific_summary(title: str, abstract: str, lowered: str) -> Optional[str]:
    stats = extract_numeric_facts(abstract)
    suffix = f"，覆盖{stats}" if stats else ""
    if "mosaic-bench" in lowered:
        return f"提出 MOSAIC-Bench，把 coding agent 的安全评测从单次提示扩展到多阶段工程任务，检查连续无害改动是否会组合成可利用漏洞{suffix}；实验还比较 staged tickets 与 direct prompt，并评估 reviewer 是否会把漏洞 PR 当作常规改动放行。"
    if "bright-pro" in lowered or "reasoning-intensive retrieval" in lowered:
        return f"提出 BRIGHT-Pro 和 RTriever-Synth，把检索评测从单段相关性改成多方面证据组合；它同时测试静态检索和 agentic search 协议，用来判断检索器能否为复杂推理持续提供互补证据{suffix}。"
    if "tracelift" in lowered or "executor-grounded rewards" in lowered:
        return "提出 TraceLift，把推理轨迹当作会被下游模块消费的中间产物：planner 生成带标签的推理，冻结 executor 执行并反馈奖励，从而避免只用最终答案正确性训练出“对但不可执行”的推理过程。"
    if "povsmith" in lowered or "proof-of-vulnerability" in lowered:
        return f"提出 PoVSmith，用调用路径分析、示例测试、代码上下文和执行反馈多轮提示 coding agent，自动生成证明依赖漏洞可达的 proof-of-vulnerability 测试{suffix}；重点是把安全告警变成开发者可运行的证据。"
    if "mcjudgebench" in lowered:
        return "提出 MCJudgeBench，把 LLM judge 评测从整体回答对错细化到每条约束是否满足；数据包含显式约束列表、逐约束 gold label 和受控扰动，用来测试 judge 在多约束指令下的正确性与稳定性。"
    if "cc-ocr v2" in lowered:
        return "提出 CC-OCR V2，面向真实企业文档处理重新设计 OCR/LMM 评测，覆盖 OCR、版面理解、表格图表读取和复杂文档读写等硬场景，强调以实际业务文档里的 corner cases 检验模型能力。"
    if "static memory safety analysis of rust" in lowered:
        return "用强化学习学习 Rust 静态内存安全分析告警的抑制策略，从 MIR 中抽取上下文特征，并结合 cargo-fuzz 动态验证可疑告警，目标是降低 Rudra/MirChecker 这类工具的误报，让开发者更信任安全扫描结果。"
    if "satformer" in lowered or "selective access transformer" in lowered:
        return "提出 SATFormer，把 Transformer 早期 value 表示的复用从静态残差改成上下文相关的门控选择；模型能按 token、head 和层深决定访问多少早期信息，在接近原始成本下改善检索密集任务。"
    if "activation steering" in lowered and "prompt" in lowered:
        return "把提示词引导重新表述为一种激活引导，发现常见 activation steering 没有复现 prompting 的 token 级干预模式；论文提出 PSR 模型学习哪些 token 需要强干预，以缩小两类方法的效果差距。"
    if "llm-powered linting" in lowered or "lintq" in lowered:
        return "把量子程序 linting 从人工维护规则改成 LLM+CoT/RAG 检测，让模型基于上下文识别快速变化 API、框架用法和量子程序特有错误，解决传统 rule-based linter 更新慢、覆盖窄的问题。"
    if "hallucination detection" in lowered or "logical consistency" in lowered:
        return "提出 LaaB，把模型回答与自我判断之间的逻辑一致性建模成桥梁：一边利用内部特征的不确定性，一边利用显式 self-judgment 标签，再通过互学习融合两类信号来提升幻觉检测。"
    if "ai-text detection" in lowered:
        return "训练带语言特征融合的 Transformer AI 文本检测器，并固定一个验证集阈值去测试跨数据集、跨领域、跨生成器迁移；重点观察真实部署时的分布偏移和错误不对称，而不是只看域内高分。"
    if "complex set-compositional information retrieval" in lowered:
        return "复现实验并扩展集合组合式检索评测，关注查询里的与、或、排除等集合约束；论文用受控 benchmark 检查检索系统是否真正满足属性约束，而不是靠预训练知识或语义捷径命中结果。"
    return None


def first_sentence(text: str) -> str:
    sentences = split_sentences(text)
    return sentences[0] if sentences else ""


def split_sentences(text: str) -> List[str]:
    normalized = " ".join(text.split())
    if not normalized:
        return []
    parts = re.split(r"(?<=[.!?])\s+", normalized)
    return [part.strip() for part in parts if len(part.strip()) > 20]


def extract_contribution_sentence(abstract: str) -> str:
    for sentence in split_sentences(abstract):
        lowered = sentence.lower()
        if any(phrase in lowered for phrase in ["we introduce", "we propose", "we present", "we created", "we construct", "we develop"]):
            return sentence
    return ""


def extract_numeric_facts(abstract: str) -> str:
    patterns = [
        r"\b\d+[\d,]*\s+three-stage attack chains",
        r"\b\d+[\d,]*\s+web-application substrates",
        r"\b\d+[\d,]*\s+CWE classes",
        r"\b\d+[\d,]*\s+programming languages",
        r"\b\d+[\d,]*\s+queries",
        r"\b\d+[\d,]*\s+tasks",
        r"\b\d+[\d,]*\s+samples",
        r"\b\d+[\d,]*\s+documents",
        r"\b\d+[\d,]*\s+constraints",
        r"\b\d+[\d,]*\s+models",
        r"\b\d+[\d,]*\s+datasets",
        r"\b\d+[\d,]*\s+test cases",
    ]
    facts: List[str] = []
    for pattern in patterns:
        match = re.search(pattern, abstract, flags=re.I)
        if match:
            facts.append(match.group(0))
        if len(facts) >= 3:
            break
    return "、".join(facts)


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
                "**摘要:**",
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


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


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
    md_path = output_dir / "daily-ai-info.md"
    legacy_md_path = output_dir / "digest-scaffold.md"
    write_json(json_path, dataset)
    md_path.write_text(scaffold, encoding="utf-8")
    legacy_md_path.write_text(scaffold, encoding="utf-8")

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
        "delivery": {
            "status": "not_sent",
            "channel": None,
            "message_ids": [],
        },
        "artifacts": {
            "daily_ai_info": str(md_path),
            "digest_data": str(json_path),
            "paper_state": args.state_file,
        },
        "logs": logs,
    }
    run_summary_path = Path(args.run_summary) if args.run_summary else output_dir / "run-log.json"
    write_json(run_summary_path, run_log)
    if args.run_log:
        append_run_log(Path(args.run_log), run_log)
    if args.index_log:
        append_run_log(
            Path(args.index_log),
            {
                "run_id": run_id,
                "status": run_log["delivery"]["status"],
                "news_count": len(news),
                "paper_selected_count": len(selected_papers),
                "path": str(run_summary_path),
                "generated_at": dataset["generated_at"],
            },
        )

    print(
        json.dumps(
            {
                "json": str(json_path),
                "markdown": str(md_path),
                "legacy_markdown": str(legacy_md_path),
                "state_file": args.state_file,
                "run_summary": str(run_summary_path),
                "run_log": args.run_log,
                "index_log": args.index_log,
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
