#streamlit run dashboard.py#
import json
import os
import streamlit as st

st.set_page_config(
    page_title="نظام تفسير أداء الطالب",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebar"] {direction: rtl;}
    .block-container {direction: rtl; text-align: right;}
    h1, h2, h3, h4, p, li, span, div {direction: rtl; text-align: right;}

    /* بطاقة المقياس */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px; padding: 24px; text-align: center;
        color: white; margin-bottom: 8px;
    }
    .metric-card.green {background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);}
    .metric-card.red   {background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);}
    .metric-card.amber {background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%);}
    .metric-value {font-size: 2.8rem; font-weight: 800; margin: 0;}
    .metric-label {font-size: 0.95rem; opacity: 0.85; margin-top: 4px;}

    /* شريط التقدم */
    .bar-bg {background: #e9ecef; border-radius: 8px; height: 22px; margin: 4px 0; overflow: hidden;}
    .bar-fill {height: 100%; border-radius: 8px; transition: width 0.6s ease;}

    /* بطاقة التوصية */
    .rec-card {
        border-radius: 12px; padding: 16px 20px; margin-bottom: 10px;
        border-right: 5px solid;
    }
    .rec-high     {background: #fff5f5; border-right-color: #e53e3e;}
    .rec-medium   {background: #fffaf0; border-right-color: #dd6b20;}
    .rec-low      {background: #f0fff4; border-right-color: #38a169;}
    .rec-critical {background: #fef2f2; border-right-color: #991b1b;}

    /* مفهوم خاطئ */
    .misc-card {
        background: #fef3c7; border-radius: 12px; padding: 14px 18px;
        margin-bottom: 8px; border-right: 4px solid #d97706;
    }
</style>
""", unsafe_allow_html=True)

from kbs import interpret, why, how_misconception
from kbs.report_generator import generate_report

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
MOCK_FILE = os.path.join(DATA_DIR, "mock_student.json")

SCENARIOS = {
    "الطالب S101 — الموضوع العام": MOCK_FILE,
    "الطالب S_ML_042 — أساسيات تعلم الآلة": os.path.join(DATA_DIR, "scenarios", "student_ml_basics.json"),
    "الطالب S_DB_017 — قواعد البيانات": os.path.join(DATA_DIR, "scenarios", "student_databases.json"),
    "الطالب S_EX_001 — طالب متقدم (متفوق)": os.path.join(DATA_DIR, "scenarios", "student_excellent.json"),
}

def metric_card(value, label, style=""):
    st.markdown(f"""
    <div class="metric-card {style}">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>""", unsafe_allow_html=True)


def progress_bar(pct, label, color="#667eea"):
    st.markdown(f"""
    <div style="margin-bottom:10px;">
        <div style="display:flex; justify-content:space-between; font-size:0.9rem; margin-bottom:2px;">
            <span style="font-weight:600;">{pct:.0f}%</span>
            <span>{label}</span>
        </div>
        <div class="bar-bg">
            <div class="bar-fill" style="width:{pct}%; background:{color};"></div>
        </div>
    </div>""", unsafe_allow_html=True)


def color_for_accuracy(acc):
    if acc >= 75:
        return "#38a169"
    if acc >= 50:
        return "#dd6b20"
    return "#e53e3e"


def level_style(level):
    if "متقدم" in (level or ""):
        return "green"
    if "متوسط" in (level or ""):
        return "amber"
    return "red"


def priority_label(p):
    return {"critical": "⚠️ حرج", "high": "🔴 عالية",
            "medium": "🟡 متوسطة", "low": "🟢 منخفضة"}.get(p, p)



with st.sidebar:
    st.markdown("## 🎓 نظام تفسير أداء الطالب")
    st.markdown("---")
    st.markdown("### 📂 مصدر البيانات")

    source = st.radio("اختاري مصدر بيانات الطالب:", ["بيانات تجريبية", "رفع ملف JSON"],
                       label_visibility="collapsed")

    attempt = None
    use_demo = False
    if source == "بيانات تجريبية":
        st.info("سيتم استخدام البيانات التجريبية المرفقة مع المشروع.")
        use_demo = True
    else:
        uploaded = st.file_uploader("ارفعي ملف JSON لمحاولة الطالب", type=["json"])
        if uploaded:
            attempt = json.load(uploaded)

    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.8rem; opacity:0.7; text-align:center;">
        مشروع مادة نظم قواعد المعرفة (KBS)<br>
        كلية الهندسة المعلوماتية — 2026/2027
    </div>
    """, unsafe_allow_html=True)


if use_demo:
    scenario_name = st.selectbox("🎯 اختاري سيناريو الطالب:", options=list(SCENARIOS.keys()))
    scenario_file = SCENARIOS[scenario_name]
    if os.path.exists(scenario_file):
        with open(scenario_file, encoding="utf-8") as f:
            attempt = json.load(f)
    else:
        st.error(f"لم يُعثر على ملف السيناريو: {scenario_file}")

if attempt is None:
    st.markdown("# 🎓 نظام تفسير أداء الطالب")
    st.markdown("ارفعي ملف محاولة الطالب من الشريط الجانبي أو اختاري البيانات التجريبية.")
    st.stop()

result = interpret(attempt)

st.markdown(f"# 📊 تقرير الطالب `{result['student_id'] or '—'}` — اختبار `{result['quiz_id'] or '—'}`")
st.markdown("---")

c1, c2, c3, c4 = st.columns(4)
with c1:
    metric_card(f"{result['score']}%", "النتيجة الكلية",
                level_style(result["level"]))
with c2:
    metric_card(result["level"] or "—", "المستوى العام",
                level_style(result["level"]))
with c3:
    metric_card(str(len(result["strengths"])), "نقاط قوة", "green")
with c4:
    metric_card(str(len(result["weaknesses"])), "نقاط ضعف",
                "red" if result["weaknesses"] else "green")

st.markdown("")

st.markdown("## 📚 أداء المواضيع")
col_topics, col_misc = st.columns([1, 1], gap="large")

with col_topics:
    sorted_topics = sorted(result["topics"], key=lambda t: t["accuracy"])
    for t in sorted_topics:
        progress_bar(t["accuracy"], t["topic_name"], color_for_accuracy(t["accuracy"]))

with col_misc:
    st.markdown("### 🔍 المفاهيم الخاطئة المكتشفة")
    if result["misconceptions"]:
        for m in sorted(result["misconceptions"], key=lambda x: -x["cf"]):
            status_text = "مؤكَّد ✅" if m["status"] == "confirmed" else "مرجَّح ⚡"
            st.markdown(f"""
            <div class="misc-card">
                <div style="font-weight:700; font-size:1rem; margin-bottom:6px;">{m['label']}</div>
                <div style="font-size:0.85rem;">
                    الحالة: {status_text} &nbsp;|&nbsp;
                    الثقة: <b>{m['cf']}</b> &nbsp;|&nbsp;
                    الأسئلة: {', '.join(m['occurrences'])}
                </div>
            </div>""", unsafe_allow_html=True)
    else:
        st.success("لم يُكتشف أي مفهوم خاطئ بثقة كافية.")

st.markdown("---")

st.markdown("## 💡 التوصيات الدراسية")
for r in result["recommendations"]:
    css = f"rec-{r['priority']}"
    st.markdown(f"""
    <div class="rec-card {css}">
        <div style="font-size:0.8rem; margin-bottom:4px;">{priority_label(r['priority'])}</div>
        <div style="font-weight:700; font-size:1.05rem; margin-bottom:6px;">{r['message']}</div>
        <div style="font-size:0.9rem; opacity:0.85;">↳ {r['explanation']}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 🧠 مرفق التفسير (Why / How)")

tab_why, tab_how = st.tabs(["🔎 لماذا هذه التوصية؟ (Why)", "🔬 كيف اكتُشف المفهوم الخاطئ؟ (How)"])

with tab_why:
    if result["recommendations"]:
        rec_options = {r["id"]: r["message"] for r in result["recommendations"]}
        selected_rec = st.selectbox("اختاري توصية:", options=list(rec_options.keys()),
                                     format_func=lambda x: rec_options[x],
                                     label_visibility="collapsed")
        if selected_rec:
            explanation = why(result, selected_rec)
            st.code(explanation, language=None)
    else:
        st.info("لا توجد توصيات للتفسير.")

with tab_how:
    if result["misconceptions"]:
        misc_options = {m["id"]: f"{m['label']} (ثقة {m['cf']})" for m in result["misconceptions"]}
        selected_misc = st.selectbox("اختاري مفهوماً خاطئاً:", options=list(misc_options.keys()),
                                      format_func=lambda x: misc_options[x],
                                      label_visibility="collapsed")
        if selected_misc:
            explanation = how_misconception(result, selected_misc)
            st.code(explanation, language=None)
    else:
        st.info("لم يُكتشف أي مفهوم خاطئ بثقة كافية.")

st.markdown("---")

with st.expander("📋 تفاصيل الإجابات (بيانات خام)"):
    for q in attempt["questions"]:
        icon = "✅" if q["is_correct"] else "❌"
        mis = q.get("selected_misconception", "none")
        mis_text = f" — المفهوم: `{mis}`" if mis not in ("none", "") and not q["is_correct"] else ""
        st.markdown(f"`{q['question_id']}` {icon} {q.get('topic_name', q['topic_id'])}{mis_text}")

st.markdown("---")

docx_bytes = generate_report(result)
st.download_button(
    label="📄 تحميل التقرير (Word)",
    data=docx_bytes,
    file_name=f"report_{result['student_id']}.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
)
