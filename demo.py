"""
عرض تشغيلي كامل للنظام الخبير على بيانات طالب وهمية.
    python demo.py
"""
import json
import os
from kbs import interpret, why, how_misconception

DATA = os.path.join(os.path.dirname(__file__), "data", "mock_student.json")


def line(c="─", n=64):
    print(c * n)


def main():
    with open(DATA, encoding="utf-8") as f:
        attempt = json.load(f)

    result = interpret(attempt)

    line("═")
    print(f"  تقرير الطالب {result['student_id']} — اختبار {result['quiz_id']}")
    line("═")
    print(f"النتيجة: {result['score']}%   |   المستوى: {result['level']}")

    print("\n● نقاط القوة:")
    for t in result["strengths"]:
        print(f"   ✓ {t['topic_name']} (دقة {t['accuracy']}%)")

    print("\n● نقاط الضعف:")
    for t in result["weaknesses"]:
        print(f"   ✗ {t['topic_name']} (دقة {t['accuracy']}%، "
              f"مفاهيمي:{t['conceptual_errors']} تطبيقي:{t['application_errors']} إهمال:{t['careless_errors']})")

    print("\n● المفاهيم الخاطئة المكتشفة:")
    for m in result["misconceptions"]:
        print(f"   • {m['label']} — {m['status']} (ثقة {m['cf']}, أسئلة: {', '.join(m['occurrences'])})")

    print("\n● التوصيات (مرتّبة حسب الأولوية):")
    for r in result["recommendations"]:
        print(f"   [{r['priority']}] {r['message']}")
        print(f"           ↳ {r['explanation']}")

    line()
    print("مثال Why  (لماذا أهم توصية؟):")
    line()
    if result["recommendations"]:
        print(why(result, result["recommendations"][0]["id"]))

    line()
    print("مثال How (كيف اكتُشف مفهوم خاطئ؟):")
    line()
    if result["misconceptions"]:
        print(how_misconception(result, result["misconceptions"][0]["id"]))


if __name__ == "__main__":
    main()
