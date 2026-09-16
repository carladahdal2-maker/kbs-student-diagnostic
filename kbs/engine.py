"""
ترتيب الأولويات (salience):
 100 تهيئة العدّادات | 90 العدّ والتجميع | 80 إنهاء الموضوع واليقين
 75 بناء المقاييس العامة | 70 جمع المواضيع | 65 المستوى | 60 تصنيف الموضوع
 55 علامة المفهوم القوي | 50 نوع الخلل | 45 التوزّع | 30 التوصيات
"""
from experta import KnowledgeEngine, Rule, NOT, MATCH, AS, TEST
from .facts import (CatalogEntry, Answer, TopicStat, Tally, Overall,
                    Evidence, Belief, StrongMisc, Level, Diagnosis, Recommendation)
from .certainty import cf_combine
from . import config as C

PER = C.CF_PER_OCCURRENCE


class KBSEngine(KnowledgeEngine):

    # ================= تهيئة العدّادات (100) ========================= #
    @Rule(Answer(topic=MATCH.t, topic_name=MATCH.n), NOT(TopicStat(topic=MATCH.t)),
          salience=100)
    def init_topic_stat(self, t, n):
        self.declare(TopicStat(topic=t, topic_name=n))

    @Rule(Answer(), NOT(Tally()), salience=100)
    def init_tally(self):
        self.declare(Tally(total=0, correct=0))

    @Rule(Evidence(mid=MATCH.m, topic=MATCH.t), NOT(Belief(mid=MATCH.m)), salience=100)
    def init_belief(self, m, t):
        self.declare(Belief(mid=m, topic=t, cf=0.0, count=0))

    # ================= العدّ والتجميع (90) =========================== #
    @Rule(AS.a << Answer(is_correct=True, topic=MATCH.t, processed=False),
          AS.s << TopicStat(topic=MATCH.t, total=MATCH.tot, correct=MATCH.cor),
          AS.g << Tally(total=MATCH.gt, correct=MATCH.gc),
          salience=90)
    def count_correct(self, a, s, g, tot, cor, gt, gc):
        self.modify(s, total=tot + 1, correct=cor + 1)
        self.modify(g, total=gt + 1, correct=gc + 1)
        self.modify(a, processed=True)

    @Rule(AS.a << Answer(is_correct=False, topic=MATCH.t, mid=MATCH.m, qid=MATCH.q,
                         misconception_detail=MATCH.d, processed=False),
          CatalogEntry(id=MATCH.m, mtype="conceptual"),
          AS.s << TopicStat(topic=MATCH.t, total=MATCH.tot, conceptual=MATCH.cc),
          AS.g << Tally(total=MATCH.gt),
          salience=90)
    def count_conceptual(self, a, s, g, t, m, q, d, tot, cc, gt):
        self.modify(s, total=tot + 1, conceptual=cc + 1)
        self.modify(g, total=gt + 1)
        self.modify(a, processed=True)
        self.declare(Evidence(mid=m, topic=t, qid=q, misconception_detail=d))

    @Rule(AS.a << Answer(is_correct=False, topic=MATCH.t, mid=MATCH.m, qid=MATCH.q,
                         misconception_detail=MATCH.d, processed=False),
          CatalogEntry(id=MATCH.m, mtype="procedural"),
          AS.s << TopicStat(topic=MATCH.t, total=MATCH.tot, procedural=MATCH.pp),
          AS.g << Tally(total=MATCH.gt),
          salience=90)
    def count_procedural(self, a, s, g, t, m, q, d, tot, pp, gt):
        self.modify(s, total=tot + 1, procedural=pp + 1)
        self.modify(g, total=gt + 1)
        self.modify(a, processed=True)
        self.declare(Evidence(mid=m, topic=t, qid=q, misconception_detail=d))

    @Rule(AS.a << Answer(is_correct=False, topic=MATCH.t, mid=MATCH.m, processed=False),
          CatalogEntry(id=MATCH.m, mtype="careless"),
          AS.s << TopicStat(topic=MATCH.t, total=MATCH.tot, careless=MATCH.kk),
          AS.g << Tally(total=MATCH.gt),
          salience=90)
    def count_careless(self, a, s, g, tot, kk, gt):
        self.modify(s, total=tot + 1, careless=kk + 1)
        self.modify(g, total=gt + 1)
        self.modify(a, processed=True)

    @Rule(AS.e << Evidence(mid=MATCH.m, misconception_detail=MATCH.d, processed=False),
          AS.b << Belief(mid=MATCH.m, cf=MATCH.cf, count=MATCH.k, misconception_detail=MATCH.bd),
          salience=90)
    def accumulate_belief(self, e, b, cf, k, d, bd):
        self.modify(b, cf=round(cf_combine(cf, PER), 3), count=k + 1,
                    misconception_detail=bd or d)
        self.modify(e, processed=True)

    # ================= إنهاء الموضوع واليقين (80) ===================== #
    @Rule(AS.s << TopicStat(topic=MATCH.t, total=MATCH.tot, correct=MATCH.cor, done=False),
          NOT(Answer(topic=MATCH.t, processed=False)),
          salience=80)
    def finalize_topic(self, s, tot, cor):
        self.modify(s, accuracy=round(cor / tot * 100, 1) if tot else 0.0, done=True)

    @Rule(AS.b << Belief(mid=MATCH.m, cf=MATCH.cf, done=False),
          NOT(Evidence(mid=MATCH.m, processed=False)),
          TEST(lambda cf: cf >= C.CF_CONFIRMED),
          salience=80)
    def belief_confirmed(self, b):
        self.modify(b, status="confirmed", done=True)

    @Rule(AS.b << Belief(mid=MATCH.m, cf=MATCH.cf, done=False),
          NOT(Evidence(mid=MATCH.m, processed=False)),
          TEST(lambda cf: C.CF_LIKELY <= cf < C.CF_CONFIRMED),
          salience=80)
    def belief_likely(self, b):
        self.modify(b, status="likely", done=True)

    @Rule(AS.b << Belief(mid=MATCH.m, cf=MATCH.cf, done=False),
          NOT(Evidence(mid=MATCH.m, processed=False)),
          TEST(lambda cf: cf < C.CF_LIKELY),
          salience=80)
    def belief_weak(self, b):
        self.modify(b, status="weak", done=True)

    # ================= بناء المقاييس العامة (75) ===================== #
    @Rule(Tally(total=MATCH.gt, correct=MATCH.gc),
          NOT(Answer(processed=False)), NOT(Overall()),
          salience=75)
    def build_overall(self, gt, gc):
        score = round(gc / gt * 100, 1) if gt else 0.0
        few = (gt - gc) <= gt * C.FEW_ERRORS_RATIO
        self.declare(Overall(score=score, few_errors=few, done=False))

    # ================= جمع المواضيع في المقاييس العامة (70) ========== #
    @Rule(AS.o << Overall(done=False, n_topics=MATCH.n, weak_count=MATCH.w),
          AS.s << TopicStat(done=True, counted=False, accuracy=MATCH.acc),
          TEST(lambda acc: acc < C.TOPIC_WEAK),
          salience=70)
    def tally_topic_weak(self, o, s, n, w):
        self.modify(o, n_topics=n + 1, weak_count=w + 1)
        self.modify(s, counted=True)

    @Rule(AS.o << Overall(done=False, n_topics=MATCH.n),
          AS.s << TopicStat(done=True, counted=False, accuracy=MATCH.acc),
          TEST(lambda acc: acc >= C.TOPIC_WEAK),
          salience=70)
    def tally_topic_nonweak(self, o, s, n):
        self.modify(o, n_topics=n + 1)
        self.modify(s, counted=True)

    @Rule(AS.o << Overall(done=False), NOT(TopicStat(counted=False)), salience=70)
    def overall_done(self, o):
        self.modify(o, done=True)

    # ================= المستوى العام (65) ============================ #
    @Rule(Overall(done=True, score=MATCH.sc), TEST(lambda sc: sc >= C.ADVANCED_LEVEL),
          salience=65)
    def level_advanced(self, sc):
        self.declare(Level(value="متقدم", justification=f"النتيجة {sc} ≥ {C.ADVANCED_LEVEL}"))

    @Rule(Overall(done=True, score=MATCH.sc),
          TEST(lambda sc: C.INTERMEDIATE_LEVEL <= sc < C.ADVANCED_LEVEL), salience=65)
    def level_intermediate(self, sc):
        self.declare(Level(value="متوسط",
                           justification=f"{C.INTERMEDIATE_LEVEL} ≤ النتيجة {sc} < {C.ADVANCED_LEVEL}"))

    @Rule(Overall(done=True, score=MATCH.sc), TEST(lambda sc: sc < C.INTERMEDIATE_LEVEL),
          salience=65)
    def level_beginner(self, sc):
        self.declare(Level(value="مبتدئ / يحتاج تأسيس",
                           justification=f"النتيجة {sc} < {C.INTERMEDIATE_LEVEL}"))

    # ================= تصنيف كل موضوع (60) =========================== #
    @Rule(TopicStat(topic=MATCH.t, done=True, accuracy=MATCH.acc),
          TEST(lambda acc: acc < C.TOPIC_WEAK), salience=60)
    def topic_weak(self, t):
        self.declare(Diagnosis(kind="weak", topic=t))

    @Rule(TopicStat(topic=MATCH.t, done=True, accuracy=MATCH.acc),
          TEST(lambda acc: C.TOPIC_WEAK <= acc < C.TOPIC_PARTIAL), salience=60)
    def topic_partial(self, t):
        self.declare(Diagnosis(kind="partial", topic=t))

    @Rule(TopicStat(topic=MATCH.t, done=True, accuracy=MATCH.acc),
          TEST(lambda acc: acc >= C.TOPIC_PARTIAL), salience=60)
    def topic_strong(self, t):
        self.declare(Diagnosis(kind="strong", topic=t))

    # ================= علامة المفهوم القوي (55) ====================== #
    @Rule(Belief(topic=MATCH.t, status=MATCH.st, done=True),
          NOT(StrongMisc(topic=MATCH.t)),
          TEST(lambda st: st in ("confirmed", "likely")), salience=55)
    def mark_strong_misc(self, t):
        self.declare(StrongMisc(topic=t))

    # ================= نوع الخلل للمواضيع الضعيفة (50) =============== #
    @Rule(Diagnosis(kind="weak", topic=MATCH.t),
          TopicStat(topic=MATCH.t, conceptual=MATCH.c, procedural=MATCH.a, careless=MATCH.k),
          TEST(lambda c, a, k: k > c + a), salience=50)
    def err_careless(self, t):
        self.declare(Diagnosis(kind="careless", topic=t))

    @Rule(Diagnosis(kind="weak", topic=MATCH.t),
          TopicStat(topic=MATCH.t, conceptual=MATCH.c, procedural=MATCH.a, careless=MATCH.k),
          TEST(lambda c, a, k: k <= c + a and (c + a) > 0 and c >= a * C.ERROR_TYPE_DOMINANT),
          salience=50)
    def err_conceptual(self, t):
        self.declare(Diagnosis(kind="conceptual", topic=t))

    @Rule(Diagnosis(kind="weak", topic=MATCH.t),
          TopicStat(topic=MATCH.t, conceptual=MATCH.c, procedural=MATCH.a, careless=MATCH.k),
          TEST(lambda c, a, k: k <= c + a and (c + a) > 0 and a >= c * C.ERROR_TYPE_DOMINANT),
          salience=50)
    def err_procedural(self, t):
        self.declare(Diagnosis(kind="procedural", topic=t))

    @Rule(Diagnosis(kind="weak", topic=MATCH.t),
          TopicStat(topic=MATCH.t, conceptual=MATCH.c, procedural=MATCH.a, careless=MATCH.k),
          TEST(lambda c, a, k: k <= c + a and (c + a) > 0
               and c < a * C.ERROR_TYPE_DOMINANT and a < c * C.ERROR_TYPE_DOMINANT),
          salience=50)
    def err_mixed(self, t):
        self.declare(Diagnosis(kind="mixed", topic=t))

    # ================= توزّع الأخطاء (45) ============================ #
    @Rule(TopicStat(topic=MATCH.t, done=True, total=MATCH.tt, correct=MATCH.tc),
          Tally(total=MATCH.gt, correct=MATCH.gc),
          NOT(Diagnosis(kind="strong", topic=MATCH.t)),
          TEST(lambda tt, tc, gt, gc: (gt - gc) > 0
               and (tt - tc) / (gt - gc) * 100 > C.CONCENTRATION),
          salience=45)
    def errors_concentrated(self, t):
        self.declare(Diagnosis(kind="concentrated", topic=t))

    @Rule(Overall(done=True, weak_count=MATCH.w),
          NOT(Diagnosis(kind="concentrated")),
          TEST(lambda w: w >= C.SPREAD_TOPICS), salience=45)
    def errors_spread(self, w):
        self.declare(Diagnosis(kind="spread", topic=""))

    # ================= حالات خاصة → توصيات (30) ===================== #
    @Rule(Overall(done=True, score=MATCH.sc), TEST(lambda sc: sc == C.PERFECT_SCORE), salience=30)
    def rec_mastery(self, sc):
        self.declare(Recommendation(rid="F1", rtype="mastery", target="all", priority="low",
                                    message="أتقنتِ هذه المادة، انتقلي للمحتوى التالي.",
                                    explanation="نتيجة كاملة دون أخطاء.", rule="F1"))

    @Rule(Overall(done=True, score=MATCH.sc, few_errors=True),
          TEST(lambda sc: sc >= C.ADVANCED_LEVEL), salience=30)
    def rec_advance(self, sc):
        self.declare(Recommendation(rid="F2", rtype="advance", target="all", priority="low",
                                    message="جرّبي أسئلة أصعب أو المحاضرة التالية.",
                                    explanation="مستواكِ متقدم وأخطاؤكِ قليلة، فالتحدّي الأعلى أنسب لكِ.",
                                    rule="F2"))

    @Rule(Overall(done=True, score=MATCH.sc, weak_count=MATCH.w, n_topics=MATCH.n),
          TEST(lambda sc, w, n: sc < C.LOW_SCORE_GAP and w == n and n > 0), salience=30)
    def rec_foundation(self):
        self.declare(Recommendation(rid="F3", rtype="foundation", target="all", priority="critical",
                                    message="ابدئي من أساسيات المادة بوتيرة أبطأ.",
                                    explanation="الضعف شامل في كل المواضيع، فالبناء من الأساس أفضل من المعالجة الجزئية.",
                                    rule="F3"))

    # ================= توليد التوصيات (30) =========================== #
    @Rule(Diagnosis(kind="weak", topic=MATCH.t),
          Belief(mid=MATCH.m, topic=MATCH.t, status=MATCH.st, cf=MATCH.cf, count=MATCH.cnt,
                 misconception_detail=MATCH.d),
          CatalogEntry(id=MATCH.m, label=MATCH.lbl, remediation=MATCH.rem),
          TEST(lambda st: st in ("confirmed", "likely")),
          TEST(lambda d: bool(d)), salience=30)
    def rec_fix_misconception_detailed(self, t, m, cf, cnt, lbl, rem, d):
        remedy = rem or "راجعي هذا المفهوم بعناية."
        self.declare(Recommendation(
            rid=f"G1:{m}", rtype="fix_misconception", target=t, priority="high",
            message=f"تصحيح: {lbl} — {d}",
            explanation=f"{remedy} ظهر هذا الخطأ في {cnt} أسئلة (ثقة {cf}).",
            rule="G1", from_kind="weak", mid=m))

    @Rule(Diagnosis(kind="weak", topic=MATCH.t),
          Belief(mid=MATCH.m, topic=MATCH.t, status=MATCH.st, cf=MATCH.cf, count=MATCH.cnt,
                 misconception_detail=MATCH.d),
          CatalogEntry(id=MATCH.m, label=MATCH.lbl, remediation=MATCH.rem),
          TEST(lambda st: st in ("confirmed", "likely")),
          TEST(lambda d: not d), salience=30)
    def rec_fix_misconception_plain(self, t, m, cf, cnt, lbl, rem):
        remedy = rem or "راجعي هذا المفهوم بعناية."
        self.declare(Recommendation(
            rid=f"G1:{m}", rtype="fix_misconception", target=t, priority="high",
            message=f"تصحيح: {lbl}",
            explanation=f"{remedy} ظهر هذا الخطأ في {cnt} أسئلة (ثقة {cf}).",
            rule="G1", from_kind="weak", mid=m))

    @Rule(Diagnosis(kind="weak", topic=MATCH.t), Diagnosis(kind="conceptual", topic=MATCH.t),
          NOT(StrongMisc(topic=MATCH.t)),
          TopicStat(topic=MATCH.t, topic_name=MATCH.n), salience=30)
    def rec_restudy_concepts(self, t, n):
        self.declare(Recommendation(
            rid=f"G2:{t}", rtype="restudy_concepts", target=t, priority="high",
            message=f"أعيدي دراسة مفاهيم «{n}».",
            explanation="أخطاؤكِ هنا فهمية لا تطبيقية، فالمشكلة في الأساس.",
            rule="G2", from_kind="conceptual"))

    @Rule(Diagnosis(kind="weak", topic=MATCH.t), Diagnosis(kind="procedural", topic=MATCH.t),
          TopicStat(topic=MATCH.t, topic_name=MATCH.n), salience=30)
    def rec_solve_exercises(self, t, n):
        self.declare(Recommendation(
            rid=f"G3:{t}", rtype="solve_exercises", target=t, priority="high",
            message=f"حُلّي تمارين إضافية على «{n}».",
            explanation="فهمكِ للمفهوم جيد لكن الأخطاء تظهر عند التطبيق؛ التمرين يعالج هذا.",
            rule="G3", from_kind="procedural"))

    @Rule(Diagnosis(kind="weak", topic=MATCH.t), Diagnosis(kind="mixed", topic=MATCH.t),
          TopicStat(topic=MATCH.t, topic_name=MATCH.n), salience=30)
    def rec_review_then_practice(self, t, n):
        self.declare(Recommendation(
            rid=f"G4:{t}", rtype="review_then_practice", target=t, priority="high",
            message=f"راجعي «{n}» ثم حُلّي تمارين عليه.",
            explanation="الأخطاء موزّعة بين الفهم والتطبيق، فالمراجعة ثم التمرين أنسب.",
            rule="G4", from_kind="mixed"))

    @Rule(Diagnosis(kind="careless", topic=MATCH.t),
          TopicStat(topic=MATCH.t, topic_name=MATCH.n), salience=30)
    def rec_careful_review(self, t, n):
        self.declare(Recommendation(
            rid=f"G5:{t}", rtype="careful_review", target=t, priority="medium",
            message=f"راجعي إجاباتكِ في «{n}» بتأنٍّ.",
            explanation="أخطاؤكِ زلّات لا ضعف معرفي؛ التروّي يكفي.",
            rule="G5", from_kind="careless"))

    @Rule(Diagnosis(kind="partial", topic=MATCH.t),
          TopicStat(topic=MATCH.t, topic_name=MATCH.n), salience=30)
    def rec_light_review(self, t, n):
        self.declare(Recommendation(
            rid=f"G6:{t}", rtype="light_review", target=t, priority="medium",
            message=f"مراجعة سريعة لـ «{n}».",
            explanation="أداؤكِ مقبول لكن قابل للتحسين بمراجعة موجزة.",
            rule="G6", from_kind="partial"))

    @Rule(Diagnosis(kind="concentrated", topic=MATCH.t),
          TopicStat(topic=MATCH.t, topic_name=MATCH.n), salience=30)
    def rec_focus_topic(self, t, n):
        self.declare(Recommendation(
            rid=f"G7:{t}", rtype="focus_topic", target=t, priority="high",
            message=f"ركّزي وقتكِ على «{n}» تحديداً.",
            explanation="أكثر من نصف أخطائكِ في هذا الموضوع، فمعالجته ترفع نتيجتكِ بسرعة.",
            rule="G7", from_kind="concentrated"))

    @Rule(Diagnosis(kind="spread"), salience=30)
    def rec_broad_review(self):
        self.declare(Recommendation(
            rid="G8", rtype="broad_review", target="all", priority="high",
            message="أعيدي مراجعة المادة بشكل عام.",
            explanation="الأخطاء منتشرة على عدة مواضيع، ما يشير لحاجة مراجعة شاملة لا نقطية.",
            rule="G8", from_kind="spread"))

    @Rule(Diagnosis(kind="strong", topic=MATCH.t),
          TopicStat(topic=MATCH.t, topic_name=MATCH.n), salience=30)
    def rec_strength(self, t, n):
        self.declare(Recommendation(
            rid=f"G9:{t}", rtype="strength", target=t, priority="low",
            message=f"«{n}» نقطة قوة لديكِ.",
            explanation="أداؤكِ ممتاز هنا؛ يمكنكِ تجاوزه والتركيز على غيره.",
            rule="G9", from_kind="strong"))
