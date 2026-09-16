"""
اختبارات النظام الخبير — الكتالوج العام (3 أنواع مفاهيم خاطئة + careless).
    python tests/test_kbs.py

mapping:
- similar_concept_confusion + cause_effect_reversal → concept_confusion (conceptual)
- overgeneralization + definition_error → conceptual_error (conceptual)
- keyword_association + partial_understanding → surface_association (procedural)
- careless 
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from kbs import interpret
from kbs.certainty import cf_combine


def _q(qid, topic, correct, mis="none"):
    return {"question_id": qid, "topic_id": topic, "topic_name": topic,
            "selected_option": "A", "correct_option": "A" if correct else "B",
            "is_correct": correct, "selected_misconception": mis}


def _acc(occurrences, per=0.4):
    cf = 0.0
    for _ in range(occurrences):
        cf = round(cf_combine(cf, per), 3)
    return cf


def test_certainty_accumulates():
    assert _acc(1) == 0.4
    assert _acc(2) == 0.64
    assert _acc(3) == 0.784
    assert _acc(5) < 1.0


def test_cf_combine_symmetry():
    assert round(cf_combine(0.4, 0.4), 2) == 0.64


def test_confirmed_misconception_drives_specific_rec():
    qs = [_q(f"q{i}", "general", False, "concept_confusion") for i in range(5)]
    r = interpret({"student_id": "M", "quiz_id": "1", "questions": qs})
    assert any(rec["type"] == "fix_misconception" for rec in r["recommendations"])
    mis = [m for m in r["misconceptions"] if m["id"] == "concept_confusion"]
    assert mis and mis[0]["status"] == "confirmed"


def test_foundation_gap():
    qs = [_q("q1", "general", False, "conceptual_error"),
          _q("q2", "general", False, "careless"),
          _q("q3", "general", False, "concept_confusion"),
          _q("q4", "general", False, "careless")]
    r = interpret({"student_id": "F", "quiz_id": "1", "questions": qs})
    assert r["level"].startswith("مبتدئ")
    assert any(rec["type"] == "foundation" for rec in r["recommendations"])


def test_perfect_score_is_mastery():
    qs = [_q(f"q{i}", "general", True) for i in range(5)]
    r = interpret({"student_id": "P", "quiz_id": "1", "questions": qs})
    assert r["score"] == 100.0
    assert any(rec["type"] == "mastery" for rec in r["recommendations"])


def test_strength_detected():
    qs = [_q(f"q{i}", "general", True) for i in range(4)] + \
         [_q("q5", "general", False, "careless")]
    r = interpret({"student_id": "S", "quiz_id": "1", "questions": qs})
    assert any(rec["type"] == "strength" for rec in r["recommendations"])


def test_partial_topic_gets_light_review():
    qs = [_q("q1", "general", True), _q("q2", "general", True),
          _q("q3", "general", False, "careless"),
          _q("q4", "general", False, "careless"),
          _q("q5", "general", True)]
    r = interpret({"student_id": "P2", "quiz_id": "1", "questions": qs})
    assert any(rec["type"] == "light_review" for rec in r["recommendations"])


def test_mixed_error_type():
    # مفاهيمي + تطبيقي بنسبة تحت ERROR_TYPE_DOMINANT → خلط مختلط
    # 4 conceptual (concept_confusion + conceptual_error) + 3 procedural (surface_association)
    qs = [_q("q1", "general", False, "concept_confusion"),      # conceptual
          _q("q2", "general", False, "surface_association"),    # procedural
          _q("q3", "general", False, "conceptual_error"),       # conceptual
          _q("q4", "general", False, "conceptual_error"),       # conceptual
          _q("q5", "general", False, "surface_association"),    # procedural
          _q("q6", "general", False, "concept_confusion"),      # conceptual
          _q("q7", "general", False, "surface_association"),    # procedural
          _q("q8", "general", True)]  # 4 conceptual, 3 procedural → mixed (ratio < 1.5)
    r = interpret({"student_id": "M2", "quiz_id": "1", "questions": qs})
    assert any(rec["type"] == "review_then_practice" for rec in r["recommendations"])


def test_concentrated_errors():
    qs = [_q("q1", "general", False, "concept_confusion"),
          _q("q2", "general", False, "concept_confusion"),
          _q("q3", "general", False, "conceptual_error"),
          _q("q4", "general", True),
          _q("q5", "general", True),
          _q("q6", "general", True)]
    r = interpret({"student_id": "C", "quiz_id": "1", "questions": qs})
    assert any(rec["type"] == "focus_topic" for rec in r["recommendations"])


def test_spread_errors():
    qs = []
    for i, t in enumerate(["t1", "t2", "t3"]):
        qs += [_q(f"q{i*2+1}", t, False, "careless"),
               _q(f"q{i*2+2}", t, False, "careless")]
    r = interpret({"student_id": "S2", "quiz_id": "1", "questions": qs})
    assert any(rec["type"] == "broad_review" for rec in r["recommendations"])


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"PASS  {fn.__name__}")
    print(f"\n{len(fns)} اختبار نجح ✓")