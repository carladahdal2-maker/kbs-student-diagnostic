"""
مرفق التفسير Why/How.
يقرأ سلسلة الاستدلال من نتيجة التشغيل (حقائق الذاكرة العاملة المُستخرَجة).
"""
from .config import CF_PER_OCCURRENCE
from .certainty import cf_combine


def why(result: dict, rec_id: str) -> str:
    """لماذا هذه التوصية؟ — يُرجع سلسلة التبرير نصاً."""
    rec = next((r for r in result["recommendations"] if r["id"] == rec_id), None)
    if not rec:
        return f"لا توجد توصية بالمعرّف {rec_id}."

    lines = [f"التوصية: {rec['message']}",
             f"  ← القاعدة {rec['rule']}.",
             f"  ← لأن: {rec['explanation']}"]

    topic = rec["target"]
    tinfo = next((t for t in result["topics"] if t["topic_id"] == topic), None)
    if tinfo:
        lines.append(f"  ← التشخيص ({rec['from_kind']}) في «{tinfo['topic_name']}»: "
                     f"دقة {tinfo['accuracy']}% "
                     f"(مفاهيمي {tinfo['conceptual_errors']}, تطبيقي {tinfo['application_errors']}, "
                     f"إهمال {tinfo['careless_errors']}).")
    if rec["evidence"]:
        lines.append(f"  ← الأسئلة الشاهدة: {', '.join(rec['evidence'])}")
    return "\n".join(lines)


def how_misconception(result: dict, misconception_id: str) -> str:
    """كيف استُنتج هذا المفهوم الخاطئ؟ — يعرض تراكم عامل اليقين خطوة بخطوة."""
    m = next((x for x in result["misconceptions"] if x["id"] == misconception_id), None)
    if not m:
        return f"لا يوجد مفهوم مؤكَّد بالمعرّف {misconception_id}."

    lines = [f"المفهوم الخاطئ: {m['label']} (الحالة: {m['status']}, الثقة {m['cf']})"]
    cf = 0.0
    for i, qid in enumerate(m["occurrences"], 1):
        cf = round(cf_combine(cf, CF_PER_OCCURRENCE), 3)
        lines.append(f"  دليل {i} (سؤال {qid}): دمج {CF_PER_OCCURRENCE} ← الثقة الآن {cf}")
    return "\n".join(lines)
