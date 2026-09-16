# دليل التكامل — KBS Interface Contract

## نظرة عامة

هذا النظام الخبير (KBS) يستقبل إجابات الطالب ويُنتج تشخيصاً 
وتوصيات تعليمية تكيّفية عبر الاستدلال الأمامي (forward chaining) 
مع عوامل اليقين (MYCIN-style certainty factors).

## Input Contract

### الصيغة المطلوبة (JSON)

```json
{
  "student_id": "string",
  "quiz_id": "string",
  "questions": [
    {
      "question_id": "string",
      "topic_id": "string",
      "topic_name": "string",
      "selected_option": "A|B|C|D",
      "correct_option": "A|B|C|D",
      "is_correct": true | false,
      "selected_misconception": "conceptual_error | surface_association | concept_confusion | careless | none",
      "misconception_detail": "string (اختياري) — سياق محدّد للخطأ"
    }
  ]
}
```

### حقل `misconception_detail` (اختياري)

نص عربي حرّ يصف **السياق المحدّد** للخطأ بدل الوصف العام وحده
(مثال: `"خلط بين التصنيف والانحدار"` بدل الاكتفاء بـ «خلط بين مفاهيم مترابطة»).

- **اختياري تماماً** — القيمة الافتراضية `""`، فالبيانات القديمة بلا هذا الحقل
  تعمل دون تغيير (backward compatible).
- يُمرَّر فقط للأسئلة الخاطئة ذات مفهوم من نوع `conceptual` أو `procedural`
  (لا يُستخدم مع `careless` أو `none`).
- يُحفَظ **أول ظهور** للسياق لكل مفهوم خاطئ، ويظهر في نهاية رسالة التوصية G1
  بالصيغة: `تصحيح: <الوصف العام> — <السياق المحدّد>`.

### قيم `selected_misconception` المقبولة

| القيمة | متى تُستخدم | mtype |
|---|---|---|
| `conceptual_error` | تعميم أو تعريف خاطئ للمفهوم | conceptual |
| `surface_association` | ربط سطحي بالكلمات أو فهم جزئي | procedural |
| `concept_confusion` | خلط بين مفاهيم مترابطة | conceptual |
| `careless` | زلّة عشوائية بدون خلل مفاهيمي | careless |
| `none` | فقط عندما `is_correct = true` | — |

⚠️ **مهم:** أي قيمة أخرى ستُتجاهل وقد تسبب فقدان معلومات تشخيصية.

## Output Contract

يُنتج النظام:

1. **Diagnosis Facts**: تشخيصات على مستوى المواضيع 
   (weak / conceptual / procedural / mixed / concentrated / spread / strong)
2. **Recommendation Facts**: توصيات تعليمية بأولويات 
   (critical / high / medium / low)
3. **Belief Facts**: عوامل يقين متراكمة لكل مفهوم خاطئ
4. **Level Fact**: تصنيف الطالب (متقدم / متوسط / مبتدئ)
5. **Explanation Trace**: تتبع أسباب كل توصية (Why-chain)

## التكامل مع مولّد أسئلة MCQ

هذا النظام مصمم للعمل مع مولّد أسئلة MCQ يُنتج، لكل مشتّت (distractor)، 
معرّف misconception يطابق أحد الأنواع الثلاثة أعلاه.

**السيناريو النموذجي:**

1. **قبل الاختبار**: MCQ Generator ينتج أسئلة، كل مشتّت مرتبط بـ `misconception_type`
2. **أثناء الاختبار**: الطالب يختار جواباً
3. **بعد الاختبار**: 
   - إذا الإجابة صحيحة → `selected_misconception = "none"`
   - إذا اختار مشتّتاً → `selected_misconception = misconception_type` لهذا المشتّت
4. **إرسال البيانات لـ KBS** → تشغيل الاستدلال → استقبال التوصيات

## تشغيل النظام

```bash
python demo.py              # تشغيل تفاعلي
python -m tests.test_kbs    # تشغيل الاختبارات
```

## الهيكلية
kbs/
├── catalog.yaml      # كتالوج المفاهيم (البيانات)
├── catalog.py        # قراءة الكتالوج
├── facts.py          # حقائق الذاكرة العاملة (Working Memory)
├── engine.py         # محرك الاستدلال + قواعد Experta
├── certainty.py      # دمج عوامل اليقين (MYCIN)
├── interpret.py      # تحويل JSON → Facts
├── explain.py        # مرفق التفسير
└── config.py         # عتبات النظام
## سجل التغييرات

### v2.1 — سياق محدّد للأخطاء + سيناريوهات جاهزة

- إضافة حقل اختياري `misconception_detail` لعقد المدخل يعرض السياق المحدّد
  للخطأ بدل الوصف العام وحده (متوافق خلفياً، الافتراضي `""`).
  ينتقل عبر `Answer → Evidence → Belief` ويظهر في رسالة التوصية G1.
- إضافة سيناريوهات طلاب جاهزة في `data/scenarios/` (ML، قواعد بيانات، طالب متفوق)
  يمكن اختيارها من مُحدِّد أعلى لوحة التحكم `dashboard.py`.

### v2.0 — Taxonomy مبني على البيانات

تم تقليص الـ taxonomy من 6 أنواع إلى 3 بناءً على تحليل كمّي 
لـ 12,000+ عينة من dataset SciQ:

- التحليل كشف أن 82% من المشتتات كانت تُصنَّف تحت 
  `overgeneralization` كافتراضي، و`similar_concept_confusion` 
  له 4 عينات فريدة فقط (غير قابل للتعلم).
- الدمج نتج عن embeddings-based heuristic (all-MiniLM-L6-v2) 
  التي التقطت العلاقات الدلالية بدقة أعلى.

الـ mapping:
- `similar_concept_confusion` + `cause_effect_reversal` → `concept_confusion`
- `overgeneralization` + `definition_error` → `conceptual_error`  
- `keyword_association` + `partial_understanding` → `surface_association`
- `careless` (بلا تغيير)