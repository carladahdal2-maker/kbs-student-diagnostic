"""
حقائق الذاكرة العاملة (Working Memory).
كل حالة النظام تُمثَّل كحقائق — لا متغيّرات بايثون لتخزين الحالة.
حقول الضبط (processed / done / counted) تمنع تكرار إطلاق القواعد بدل حلقات التحكم.
"""
from experta import Fact, Field


class CatalogEntry(Fact):
    """مدخل من كتالوج المفاهيم الخاطئة (المعرفة كحقائق)."""
    id = Field(str, mandatory=True)
    mtype = Field(str, mandatory=True)        # conceptual | procedural | careless
    label = Field(str, default="")
    remediation = Field(str, default="")


class Answer(Fact):
    """إجابة الطالب الخام على سؤال واحد."""
    qid = Field(str, mandatory=True)
    topic = Field(str, mandatory=True)
    topic_name = Field(str, default="")
    is_correct = Field(bool, mandatory=True)
    mid = Field(str, default="none")          
    misconception_detail = Field(str, default="") 
    processed = Field(bool, default=False)


class TopicStat(Fact):
    """إحصاء موضوع، يتراكم عبر القواعد بدل حلقة."""
    topic = Field(str, mandatory=True)
    topic_name = Field(str, default="")
    total = Field(int, default=0)
    correct = Field(int, default=0)
    conceptual = Field(int, default=0)
    procedural = Field(int, default=0)
    careless = Field(int, default=0)
    accuracy = Field(float, default=0.0)
    done = Field(bool, default=False)
    counted = Field(bool, default=False)


class Tally(Fact):
    """العدّاد العام (مجموع كل المواضيع)."""
    total = Field(int, default=0)
    correct = Field(int, default=0)


class Overall(Fact):
    """المقاييس العامة، تُبنى بعد انتهاء العدّ."""
    score = Field(float, default=0.0)
    n_topics = Field(int, default=0)
    weak_count = Field(int, default=0)
    few_errors = Field(bool, default=False)
    done = Field(bool, default=False)


class Evidence(Fact):
    """دليل واحد على مفهوم خاطئ (ظهور في سؤال)."""
    mid = Field(str, mandatory=True)
    topic = Field(str, mandatory=True)
    qid = Field(str, mandatory=True)
    misconception_detail = Field(str, default="")  
    processed = Field(bool, default=False)


class Belief(Fact):
    """اعتقاد بوجود مفهوم خاطئ مع عامل يقينه المتراكم."""
    mid = Field(str, mandatory=True)
    topic = Field(str, mandatory=True)
    cf = Field(float, default=0.0)
    count = Field(int, default=0)
    status = Field(str, default="")           # confirmed | likely | weak
    misconception_detail = Field(str, default="") 
    done = Field(bool, default=False)


class StrongMisc(Fact):
    """علامة: الموضوع فيه مفهوم خاطئ مؤكَّد/مرجَّح (تُستخدم في NOT)."""
    topic = Field(str, mandatory=True)


class Level(Fact):
    """المستوى العام للطالب."""
    value = Field(str, mandatory=True)
    justification = Field(str, default="")


class Diagnosis(Fact):
    """تشخيص وسيط تتفاعل معه قواعد التوصية."""
    kind = Field(str, mandatory=True)         # weak|partial|strong|conceptual|...
    topic = Field(str, default="")


class Recommendation(Fact):
    """توصية نهائية مع تفسيرها — مخزّنة كحقيقة."""
    rid = Field(str, mandatory=True)
    rtype = Field(str, mandatory=True)
    target = Field(str, default="")
    priority = Field(str, default="medium")
    message = Field(str, default="")
    explanation = Field(str, default="")
    rule = Field(str, default="")
    from_kind = Field(str, default="")        # نوع التشخيص الذي ولّدها (لـ Why)
    mid = Field(str, default="")              # المفهوم الخاطئ المرتبط (لجمع الأدلة)
