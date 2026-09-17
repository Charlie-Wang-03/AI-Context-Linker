"""A packaged first-run demo, using only fictional facts and the real compiler."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from .core import BundlePaths, ManifestError, build_bundle, prepare_document, validate_output_directory


def demo_manifest() -> dict:
    captured = "2026-09-17T09:00:00+08:00"
    projects = []
    scenarios = [
        ("recipe-notebook", "食谱笔记", "把试做过的菜谱整理成可检索的个人笔记。",
         "搜索已经可用，但还没有找人试用。", "请一位朋友用三道菜测试搜索，记录找不到的词。"),
        ("weekend-map", "周末地图", "整理周末想去的地点，方便和朋友讨论行程。",
         "已有地点清单，同行者的时间还未确定。", "向同行者确认周六还是周日有空。"),
    ]
    for index, (project_id, name, summary, blocker, action) in enumerate(scenarios):
        records = []
        for offset, (kind, text) in enumerate([
            ("current-goal", summary), ("blocker", blocker), ("next-action", action),
        ]):
            evidence = f"{project_id}:synthetic-review:{kind}"
            records.append({
                "record_id": f"state-{index * 10 + offset + 1:016d}",
                "kind": kind, "text": text, "status": "open",
                "source_kind": "approved-review", "source_ref": evidence,
                "observed_at": captured, "expires_at": "2026-09-24T09:00:00+08:00",
                "supersedes": [], "freshness": "current", "evidence": evidence,
                "provenance": "approved-review",
            })
        projects.append({
            "id": project_id, "name": name, "summary": summary,
            "status": "虚构演示项目 / Fictional demo project",
            "sensitivity": "public", "cloud_visibility": "allow", "redaction_profile": "standard",
            "signals": [], "risks": [], "constraints": [], "open_questions": [],
            "state_items": records, "evidence": [f"{project_id}:synthetic:README.md"],
            "attached_documents": [prepare_document(
                "README.md", f"# {name}\n\n虚构演示资料，不代表真实用户或运行验证。\n\n{summary}\n",
            )],
        })
    return {
        "schema_version": "0.2", "generated_at": captured,
        "workspace": {
            "name": "虚构项目演示 / Synthetic demo",
            "summary": "以下全部是内置虚构资料。没有读取本机项目，没有联网或上传。",
            "current_focus": "体验一份可交给聊天的项目简报。",
            "decisions": ["只按演示快照讨论；示例中的批准记录不代表真实用户批准。"],
            "unknowns": ["用户真正的项目、优先级和最新进展均未知。"],
        },
        "projects": projects, "relationships": [],
    }


def build_demo(output_dir: Path | str) -> BundlePaths:
    destination = validate_output_directory(output_dir)
    if destination.exists():
        raise ManifestError("demo requires a new output directory; choose another path to preserve existing files")
    # Reserve the destination without replacing an existing bundle, even on a repeated run.
    destination.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix="ai-context-linker-demo-") as temporary:
        manifest = Path(temporary) / "synthetic.json"
        manifest.write_text(json.dumps(demo_manifest(), ensure_ascii=False), encoding="utf-8")
        return build_bundle(manifest, destination)
