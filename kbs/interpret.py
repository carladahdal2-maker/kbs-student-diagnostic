"""
الواجهة العامة. 
"""
from .engine import KBSEngine
from .facts import (CatalogEntry, Answer, TopicStat, Tally, Overall,
                    Evidence, Belief, Level, Diagnosis, Recommendation)
from .catalog import default_catalog
from . import config as C

_PRIORITY = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def _by_type(engine, cls):
    return [f for f in engine.facts.values() if isinstance(f, cls)]


def interpret(attempt: dict, catalog=default_catalog) -> dict:
    engine = KBSEngine()
    engine.reset()

    # --- تهيئة الذاكرة العاملة: الكتالوج كحقائق ---
    for entry in catalog.by_id.values():
        engine.declare(CatalogEntry(
            id=entry["id"], mtype=entry["type"],
            label=entry.get("label") or "", remediation=entry.get("remediation") or ""))

    # --- إجابات الطالب كحقائق (مع تطبيع المفهوم غير المعروف إلى careless) ---
    for q in attempt["questions"]:
        mid = q.get("selected_misconception", "none")
        if not q["is_correct"] and mid not in catalog.by_id:
            mid = "careless"
        engine.declare(Answer(
            qid=q["question_id"], topic=q["topic_id"],
            topic_name=q.get("topic_name", q["topic_id"]),
            is_correct=bool(q["is_correct"]), mid=mid,
            misconception_detail=q.get("misconception_detail", "")))

    engine.run()

    # --- قراءة النتائج من الذاكرة العاملة ---
    tally = _by_type(engine, Tally)
    total_q = tally[0]["total"] if tally else 0
    total_correct = tally[0]["correct"] if tally else 0
    total_errors = total_q - total_correct

    topics = []
    for s in _by_type(engine, TopicStat):
        errors = s["total"] - s["correct"]
        topics.append({
            "topic_id": s["topic"], "topic_name": s["topic_name"],
            "accuracy": s["accuracy"], "total": s["total"], "correct": s["correct"],
            "conceptual_errors": s["conceptual"], "application_errors": s["procedural"],
            "careless_errors": s["careless"],
            "error_share": round(errors / total_errors * 100, 1) if total_errors else 0.0,
        })

    # أدلة كل مفهوم
    evidence_by_mid = {}
    for e in _by_type(engine, Evidence):
        evidence_by_mid.setdefault(e["mid"], []).append(e["qid"])

    misconceptions = []
    for b in _by_type(engine, Belief):
        entry = catalog.get(b["mid"]) or {}
        misconceptions.append({
            "id": b["mid"], "topic_id": b["topic"], "label": entry.get("label", b["mid"]),
            "cf": b["cf"], "status": b["status"],
            "occurrences": sorted(evidence_by_mid.get(b["mid"], [])),
        })

    recs = []
    for r in _by_type(engine, Recommendation):
        recs.append({
            "id": r["rid"], "type": r["rtype"], "target": r["target"],
            "priority": r["priority"], "message": r["message"],
            "explanation": r["explanation"], "rule": r["rule"],
            "from_kind": r["from_kind"], "mid": r["mid"],
            "evidence": sorted(evidence_by_mid.get(r["mid"], [])) if r["mid"] else [],
        })
    recs.sort(key=lambda r: _PRIORITY.get(r["priority"], 9))

    levels = _by_type(engine, Level)
    diagnoses = [{"kind": d["kind"], "topic": d["topic"]} for d in _by_type(engine, Diagnosis)]

    return {
        "student_id": attempt.get("student_id"),
        "quiz_id": attempt.get("quiz_id"),
        "score": round(total_correct / total_q * 100, 1) if total_q else 0.0,
        "level": levels[0]["value"] if levels else None,
        "_level_just": levels[0]["justification"] if levels else None,
        "topics": topics,
        "strengths": [t for t in topics if t["accuracy"] >= C.TOPIC_PARTIAL],
        "weaknesses": [t for t in topics if t["accuracy"] < C.TOPIC_WEAK],
        "misconceptions": [m for m in misconceptions if m["status"] != "weak"],
        "recommendations": recs,
        "_diagnoses": diagnoses,
    }
