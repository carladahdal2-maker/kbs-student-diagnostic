# 📁 PROJECT EXPORT FOR LLMs

## 📊 Project Information

- **Project Name**: `kbs_project`
- **Generated On**: 2026-09-16 18:55:36 (America/Los_Angeles / GMT-07:00)
- **Total Files Processed**: 29
- **Export Tool**: Easy Whole Project to Single Text File for LLMs v1.1.0
- **Tool Author**: Jota / José Guilherme Pandolfi

### ⚙️ Export Configuration

| Setting | Value |
|---------|-------|
| Language | `en` |
| Max File Size | `1 MB` |
| Include Hidden Files | `false` |
| Output Format | `both` |

## 🌳 Project Structure

```
├── 📁 data/
│   ├── 📁 scenarios/
│   │   ├── 📄 student_databases.json (4.18 KB)
│   │   ├── 📄 student_excellent.json (3.16 KB)
│   │   └── 📄 student_ml_basics.json (4.42 KB)
│   └── 📄 mock_student.json (3.08 KB)
├── 📁 kbs/
│   ├── 📁 __pycache__/
│   │   ├── 📄 __init__.cpython-39.pyc (273 B)
│   │   ├── 📄 catalog.cpython-39.pyc (1.36 KB)
│   │   ├── 📄 certainty.cpython-39.pyc (536 B)
│   │   ├── 📄 config.cpython-39.pyc (566 B)
│   │   ├── 📄 engine.cpython-39.pyc (17.86 KB)
│   │   ├── 📄 explain.cpython-39.pyc (2.61 KB)
│   │   ├── 📄 facts.cpython-39.pyc (4.44 KB)
│   │   ├── 📄 interpret.cpython-39.pyc (3.59 KB)
│   │   └── 📄 report_generator.cpython-39.pyc (5.73 KB)
│   ├── 📄 __init__.py (130 B)
│   ├── 📄 catalog.py (1.02 KB)
│   ├── 📄 catalog.yaml (1.07 KB)
│   ├── 📄 certainty.py (395 B)
│   ├── 📄 config.py (408 B)
│   ├── 📄 engine.py (18.31 KB)
│   ├── 📄 explain.py (2.04 KB)
│   ├── 📄 facts.py (3.83 KB)
│   ├── 📄 interpret.py (3.92 KB)
│   └── 📄 report_generator.py (8.94 KB)
├── 📁 tests/
│   └── 📄 test_kbs.py (4.95 KB)
├── 📄 dashboard.py (9.95 KB)
├── 📄 demo.py (1.91 KB)
├── 📄 INTEGRATION.md (6.02 KB)
├── 📄 README.md (5.68 KB)
└── 📄 requirements.txt (271 B)
```

## 📑 Table of Contents

**Project Files:**

- [📄 data/scenarios/student_databases.json](#📄-data-scenarios-student-databases-json)
- [📄 data/scenarios/student_excellent.json](#📄-data-scenarios-student-excellent-json)
- [📄 data/scenarios/student_ml_basics.json](#📄-data-scenarios-student-ml-basics-json)
- [📄 data/mock_student.json](#📄-data-mock-student-json)
- [📄 kbs/__init__.py](#📄-kbs-init-py)
- [📄 kbs/catalog.py](#📄-kbs-catalog-py)
- [📄 kbs/catalog.yaml](#📄-kbs-catalog-yaml)
- [📄 kbs/certainty.py](#📄-kbs-certainty-py)
- [📄 kbs/config.py](#📄-kbs-config-py)
- [📄 kbs/engine.py](#📄-kbs-engine-py)
- [📄 kbs/explain.py](#📄-kbs-explain-py)
- [📄 kbs/facts.py](#📄-kbs-facts-py)
- [📄 kbs/interpret.py](#📄-kbs-interpret-py)
- [📄 kbs/report_generator.py](#📄-kbs-report-generator-py)
- [📄 tests/test_kbs.py](#📄-tests-test-kbs-py)
- [📄 dashboard.py](#📄-dashboard-py)
- [📄 demo.py](#📄-demo-py)
- [📄 INTEGRATION.md](#📄-integration-md)
- [📄 README.md](#📄-readme-md)
- [📄 requirements.txt](#📄-requirements-txt)

---

## 📈 Project Statistics

| Metric | Count |
|--------|-------|
| Total Files | 29 |
| Total Directories | 5 |
| Text Files | 20 |
| Binary Files | 9 |
| Total Size | 120.59 KB |

### 📄 File Types Distribution

| Extension | Count |
|-----------|-------|
| `.py` | 12 |
| `.pyc` | 9 |
| `.json` | 4 |
| `.md` | 2 |
| `.yaml` | 1 |
| `.txt` | 1 |

## 💻 File Code Contents

### <a id="📄-data-scenarios-student-databases-json"></a>📄 `data/scenarios/student_databases.json`

**File Info:**
- **Size**: 4.18 KB
- **Extension**: `.json`
- **Language**: `json`
- **Location**: `data/scenarios/student_databases.json`
- **Relative Path**: `data/scenarios`
- **Created**: 2026-07-04 08:22:36 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-04 08:22:36 (America/Los_Angeles / GMT-07:00)
- **MD5**: `2be75b9d61a355efe49fe8d590e9c612`
- **SHA256**: `327344b698fc73fe3440f60aef69c01c65e51885ec5dd1a28ce6cd76fb8a8293`
- **Encoding**: UTF-8

**File code content:**

```json
{
    "student_id": "S_DB_017",
    "quiz_id": "Database_Systems_Quiz",
    "questions": [
        {
            "question_id": "q1",
            "topic_id": "normalization",
            "topic_name": "التطبيع",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q2",
            "topic_id": "normalization",
            "topic_name": "التطبيع",
            "selected_option": "B",
            "correct_option": "C",
            "is_correct": false,
            "selected_misconception": "surface_association",
            "misconception_detail": "الاعتماد على شكل الجدول بدل تحليل الاعتماديات"
        },
        {
            "question_id": "q3",
            "topic_id": "normalization",
            "topic_name": "التطبيع",
            "selected_option": "D",
            "correct_option": "A",
            "is_correct": false,
            "selected_misconception": "surface_association",
            "misconception_detail": "الاعتماد على شكل الجدول بدل تحليل الاعتماديات"
        },
        {
            "question_id": "q4",
            "topic_id": "sql_queries",
            "topic_name": "استعلامات SQL",
            "selected_option": "C",
            "correct_option": "A",
            "is_correct": false,
            "selected_misconception": "surface_association",
            "misconception_detail": "استخدام JOIN بدون فهم نوعه الصحيح"
        },
        {
            "question_id": "q5",
            "topic_id": "sql_queries",
            "topic_name": "استعلامات SQL",
            "selected_option": "B",
            "correct_option": "D",
            "is_correct": false,
            "selected_misconception": "surface_association",
            "misconception_detail": "استخدام JOIN بدون فهم نوعه الصحيح"
        },
        {
            "question_id": "q6",
            "topic_id": "sql_queries",
            "topic_name": "استعلامات SQL",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q7",
            "topic_id": "transactions",
            "topic_name": "المعاملات",
            "selected_option": "B",
            "correct_option": "B",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q8",
            "topic_id": "transactions",
            "topic_name": "المعاملات",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q9",
            "topic_id": "transactions",
            "topic_name": "المعاملات",
            "selected_option": "C",
            "correct_option": "D",
            "is_correct": false,
            "selected_misconception": "conceptual_error",
            "misconception_detail": "خلط في مفهوم ACID properties"
        },
        {
            "question_id": "q10",
            "topic_id": "indexing",
            "topic_name": "الفهرسة",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q11",
            "topic_id": "indexing",
            "topic_name": "الفهرسة",
            "selected_option": "B",
            "correct_option": "B",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q12",
            "topic_id": "indexing",
            "topic_name": "الفهرسة",
            "selected_option": "D",
            "correct_option": "C",
            "is_correct": false,
            "selected_misconception": "careless"
        }
    ]
}
```

---

### <a id="📄-data-scenarios-student-excellent-json"></a>📄 `data/scenarios/student_excellent.json`

**File Info:**
- **Size**: 3.16 KB
- **Extension**: `.json`
- **Language**: `json`
- **Location**: `data/scenarios/student_excellent.json`
- **Relative Path**: `data/scenarios`
- **Created**: 2026-07-04 07:47:21 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-04 07:47:36 (America/Los_Angeles / GMT-07:00)
- **MD5**: `22d406dde6fbd92b74ab1e36d0524d49`
- **SHA256**: `f5c77d2ebce4f9629afd5e530ff4fb867b2e12a323a492ed338f9ea3cb1644b0`
- **Encoding**: UTF-8

**File code content:**

```json
{
    "student_id": "S_EX_001",
    "quiz_id": "AI_Advanced_Quiz",
    "questions": [
        {
            "question_id": "q1",
            "topic_id": "deep_learning",
            "topic_name": "التعلم العميق",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q2",
            "topic_id": "deep_learning",
            "topic_name": "التعلم العميق",
            "selected_option": "B",
            "correct_option": "B",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q3",
            "topic_id": "deep_learning",
            "topic_name": "التعلم العميق",
            "selected_option": "C",
            "correct_option": "C",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q4",
            "topic_id": "computer_vision",
            "topic_name": "الرؤية الحاسوبية",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q5",
            "topic_id": "computer_vision",
            "topic_name": "الرؤية الحاسوبية",
            "selected_option": "D",
            "correct_option": "D",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q6",
            "topic_id": "computer_vision",
            "topic_name": "الرؤية الحاسوبية",
            "selected_option": "B",
            "correct_option": "B",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q7",
            "topic_id": "nlp",
            "topic_name": "معالجة اللغات الطبيعية",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q8",
            "topic_id": "nlp",
            "topic_name": "معالجة اللغات الطبيعية",
            "selected_option": "C",
            "correct_option": "C",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q9",
            "topic_id": "nlp",
            "topic_name": "معالجة اللغات الطبيعية",
            "selected_option": "D",
            "correct_option": "B",
            "is_correct": false,
            "selected_misconception": "careless"
        },
        {
            "question_id": "q10",
            "topic_id": "reinforcement_learning",
            "topic_name": "التعلم المعزَّز",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        }
    ]
}
```

---

### <a id="📄-data-scenarios-student-ml-basics-json"></a>📄 `data/scenarios/student_ml_basics.json`

**File Info:**
- **Size**: 4.42 KB
- **Extension**: `.json`
- **Language**: `json`
- **Location**: `data/scenarios/student_ml_basics.json`
- **Relative Path**: `data/scenarios`
- **Created**: 2026-07-04 08:21:57 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-04 08:21:57 (America/Los_Angeles / GMT-07:00)
- **MD5**: `2c67f803075dab37a2b14369118e9f20`
- **SHA256**: `58f20808309a1fcc935fec8335646856ff5f4e5ba51027adab5053e937408a14`
- **Encoding**: UTF-8

**File code content:**

```json
{
    "student_id": "S_ML_042",
    "quiz_id": "ML_Fundamentals_Quiz",
    "questions": [
        {
            "question_id": "q1",
            "topic_id": "supervised_learning",
            "topic_name": "التعلم الموجّه",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q2",
            "topic_id": "supervised_learning",
            "topic_name": "التعلم الموجّه",
            "selected_option": "C",
            "correct_option": "A",
            "is_correct": false,
            "selected_misconception": "concept_confusion",
            "misconception_detail": "خلط بين التصنيف والانحدار"
        },
        {
            "question_id": "q3",
            "topic_id": "supervised_learning",
            "topic_name": "التعلم الموجّه",
            "selected_option": "B",
            "correct_option": "D",
            "is_correct": false,
            "selected_misconception": "concept_confusion",
            "misconception_detail": "خلط بين التصنيف والانحدار"
        },
        {
            "question_id": "q4",
            "topic_id": "neural_networks",
            "topic_name": "الشبكات العصبية",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q5",
            "topic_id": "neural_networks",
            "topic_name": "الشبكات العصبية",
            "selected_option": "B",
            "correct_option": "A",
            "is_correct": false,
            "selected_misconception": "conceptual_error",
            "misconception_detail": "تعميم خاطئ لدور Activation Function"
        },
        {
            "question_id": "q6",
            "topic_id": "neural_networks",
            "topic_name": "الشبكات العصبية",
            "selected_option": "D",
            "correct_option": "C",
            "is_correct": false,
            "selected_misconception": "conceptual_error",
            "misconception_detail": "تعميم خاطئ لدور Activation Function"
        },
        {
            "question_id": "q7",
            "topic_id": "model_evaluation",
            "topic_name": "تقييم النماذج",
            "selected_option": "A",
            "correct_option": "A",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q8",
            "topic_id": "model_evaluation",
            "topic_name": "تقييم النماذج",
            "selected_option": "B",
            "correct_option": "B",
            "is_correct": true,
            "selected_misconception": "none"
        },
        {
            "question_id": "q9",
            "topic_id": "model_evaluation",
            "topic_name": "تقييم النماذج",
            "selected_option": "C",
            "correct_option": "A",
            "is_correct": false,
            "selected_misconception": "surface_association",
            "misconception_detail": "ربط بكلمة accuracy بدون فهم الـ imbalanced data"
        },
        {
            "question_id": "q10",
            "topic_id": "regularization",
            "topic_name": "التنظيم",
            "selected_option": "B",
            "correct_option": "A",
            "is_correct": false,
            "selected_misconception": "concept_confusion",
            "misconception_detail": "خلط بين L1 و L2 regularization"
        },
        {
            "question_id": "q11",
            "topic_id": "regularization",
            "topic_name": "التنظيم",
            "selected_option": "C",
            "correct_option": "D",
            "is_correct": false,
            "selected_misconception": "concept_confusion",
            "misconception_detail": "خلط بين L1 و L2 regularization"
        },
        {
            "question_id": "q12",
            "topic_id": "regularization",
            "topic_name": "التنظيم",
            "selected_option": "A",
            "correct_option": "B",
            "is_correct": false,
            "selected_misconception": "careless"
        }
    ]
}
```

---

### <a id="📄-data-mock-student-json"></a>📄 `data/mock_student.json`

**File Info:**
- **Size**: 3.08 KB
- **Extension**: `.json`
- **Language**: `json`
- **Location**: `data/mock_student.json`
- **Relative Path**: `data`
- **Created**: 2026-07-04 08:21:00 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-04 08:21:00 (America/Los_Angeles / GMT-07:00)
- **MD5**: `93395b99a00694c7133b2366d9b6b968`
- **SHA256**: `e949e1d46a2433a2635934dfeca97f8e80a264c43ffba05d3927d00b276ab8ac`
- **Encoding**: UTF-8

**File code content:**

```json
{
  "student_id": "S101",
  "quiz_id": "General_Quiz_01",
  "questions": [
    {
      "question_id": "q1",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "A",
      "correct_option": "A",
      "is_correct": true,
      "selected_misconception": "none"
    },
    {
      "question_id": "q2",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "B",
      "correct_option": "A",
      "is_correct": false,
      "selected_misconception": "concept_confusion",
      "misconception_detail": "خلط بين مفهومين مترابطين في الموضوع"
    },
    {
      "question_id": "q3",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "C",
      "correct_option": "A",
      "is_correct": false,
      "selected_misconception": "concept_confusion",
      "misconception_detail": "خلط بين تعريفين متشابهين"
    },
    {
      "question_id": "q4",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "D",
      "correct_option": "B",
      "is_correct": false,
      "selected_misconception": "surface_association",
      "misconception_detail": "اعتماد على كلمة مفتاحية دون فهم السياق"
    },
    {
      "question_id": "q5",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "B",
      "correct_option": "C",
      "is_correct": false,
      "selected_misconception": "concept_confusion",
      "misconception_detail": "خلط في العلاقة السببية بين المفهومين"
    },
    {
      "question_id": "q6",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "A",
      "correct_option": "D",
      "is_correct": false,
      "selected_misconception": "conceptual_error",
      "misconception_detail": "تعميم خاطئ لقاعدة خارج شروط تطبيقها"
    },
    {
      "question_id": "q7",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "A",
      "correct_option": "A",
      "is_correct": true,
      "selected_misconception": "none"
    },
    {
      "question_id": "q8",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "B",
      "correct_option": "B",
      "is_correct": true,
      "selected_misconception": "none"
    },
    {
      "question_id": "q9",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "C",
      "correct_option": "B",
      "is_correct": false,
      "selected_misconception": "concept_confusion",
      "misconception_detail": "خلط بين مفهومين متقاربين"
    },
    {
      "question_id": "q10",
      "topic_id": "general",
      "topic_name": "الموضوع العام",
      "selected_option": "A",
      "correct_option": "C",
      "is_correct": false,
      "selected_misconception": "careless"
    }
  ]
}
```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `kbs/__pycache__/__init__.cpython-39.pyc`
- `kbs/__pycache__/catalog.cpython-39.pyc`
- `kbs/__pycache__/certainty.cpython-39.pyc`
- `kbs/__pycache__/config.cpython-39.pyc`
- `kbs/__pycache__/engine.cpython-39.pyc`
- `kbs/__pycache__/explain.cpython-39.pyc`
- `kbs/__pycache__/facts.cpython-39.pyc`
- `kbs/__pycache__/interpret.cpython-39.pyc`
- `kbs/__pycache__/report_generator.cpython-39.pyc`

### <a id="📄-kbs-init-py"></a>📄 `kbs/__init__.py`

**File Info:**
- **Size**: 130 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/__init__.py`
- **Relative Path**: `kbs`
- **Created**: 2026-06-28 17:38:23 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:09:30 (America/Los_Angeles / GMT-07:00)
- **MD5**: `e6b5bf3f4e9395a09063c16e9c550f98`
- **SHA256**: `f748bdb2c8ab3e396fcaaee8b626d21eb27de1249513984fe749746f2fd9598a`
- **Encoding**: ASCII

**File code content:**

```python
from .interpret import interpret
from .explain import why, how_misconception

__all__ = ["interpret", "why", "how_misconception"]

```

---

### <a id="📄-kbs-catalog-py"></a>📄 `kbs/catalog.py`

**File Info:**
- **Size**: 1.02 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/catalog.py`
- **Relative Path**: `kbs`
- **Created**: 2026-06-28 17:38:23 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:55:17 (America/Los_Angeles / GMT-07:00)
- **MD5**: `a41bc81507871d07d32baaf33326dc85`
- **SHA256**: `ac6ba85b6b3e06809215d35b3b9529b240d366f5538b981165d47fc1c7a72901`
- **Encoding**: UTF-8

**File code content:**

```python
"""
محمّل كتالوج المفاهيم الخاطئة.
"""
import os
import yaml

_CATALOG_PATH = os.path.join(os.path.dirname(__file__), "catalog.yaml")


class Catalog:
    def __init__(self, path: str = _CATALOG_PATH):
        with open(path, encoding="utf-8") as f:
            raw = yaml.safe_load(f)
        self.by_topic = raw                    
        self.by_id = {}                       
        for topic_id, items in raw.items():
            for item in items:
                entry = dict(item)
                entry["topic_id"] = topic_id
                self.by_id[item["id"]] = entry

    def get(self, misconception_id: str):
        """يُرجع تعريف المفهوم الخاطئ أو None."""
        return self.by_id.get(misconception_id)

    def type_of(self, misconception_id: str) -> str:
        """نوع المفهوم: conceptual | procedural | careless | unknown."""
        entry = self.by_id.get(misconception_id)
        return entry["type"] if entry else "unknown"


default_catalog = Catalog()

```

---

### <a id="📄-kbs-catalog-yaml"></a>📄 `kbs/catalog.yaml`

**File Info:**
- **Size**: 1.07 KB
- **Extension**: `.yaml`
- **Language**: `yaml`
- **Location**: `kbs/catalog.yaml`
- **Relative Path**: `kbs`
- **Created**: 2026-06-28 17:38:23 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:13:31 (America/Los_Angeles / GMT-07:00)
- **MD5**: `bf7c53c230ba8e66db4255667b60b2ae`
- **SHA256**: `a06de780545b8b1f3c331650c207689b08ff604fb3d1366537e99fab73b2fc54`
- **Encoding**: UTF-8

**File code content:**

```yaml
general:
  - id: conceptual_error
    type: conceptual
    label: "خطأ مفهومي (تعميم أو تعريف خاطئ)"
    remediation: "راجعي التعريف الدقيق للمفهوم من المصدر الأساسي، وتحققي من شروط تطبيق القاعدة قبل استخدامها."

  - id: surface_association
    type: procedural
    label: "ربط سطحي (بكلمات مفتاحية أو فهم جزئي)"
    remediation: "لا تعتمدي على الكلمات المفتاحية فقط؛ تمرّني على تطبيق المفهوم في سياقات مختلفة وابحثي عن الحالات الاستثنائية."

  - id: concept_confusion
    type: conceptual
    label: "خلط بين مفاهيم مترابطة (متشابهة أو سببياً)"
    remediation: "قارني بين المفاهيم المترابطة مباشرة — اكتبي تعريف كل منها وحدد العلاقة السببية بينها بوضوح."

  - id: careless
    type: careless
    label: "زلّة غير مفاهيمية"
    remediation: null
```

---

### <a id="📄-kbs-certainty-py"></a>📄 `kbs/certainty.py`

**File Info:**
- **Size**: 395 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/certainty.py`
- **Relative Path**: `kbs`
- **Created**: 2026-06-28 17:38:23 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:14:44 (America/Los_Angeles / GMT-07:00)
- **MD5**: `900c21f0fa3c83675d9d614660c0133c`
- **SHA256**: `74fa1b88f094332342a097398e4b6a59900476136886173854bd9194add29925`
- **Encoding**: UTF-8

**File code content:**

```python
def cf_combine(cf1: float, cf2: float) -> float:
    """دمج دليلين حسب قواعد MYCIN (موجب/موجب، سالب/سالب، مختلفان)."""
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    if cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    denom = 1 - min(abs(cf1), abs(cf2))
    return (cf1 + cf2) / denom if denom != 0 else (cf1 + cf2)

```

---

### <a id="📄-kbs-config-py"></a>📄 `kbs/config.py`

**File Info:**
- **Size**: 408 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/config.py`
- **Relative Path**: `kbs`
- **Created**: 2026-06-28 17:38:23 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:56:02 (America/Los_Angeles / GMT-07:00)
- **MD5**: `4c8dfd3b2d7c6ff0d39bf0d94e7d31ae`
- **SHA256**: `8167e4df04be44bd3e177fe3fa53142aca51a8f668f4cc8a5c57936afa84cff2`
- **Encoding**: UTF-8

**File code content:**

```python
"""
إعدادات النظام(العتبات) .
"""

ADVANCED_LEVEL = 85       
INTERMEDIATE_LEVEL = 60   

TOPIC_WEAK = 50           
TOPIC_PARTIAL = 75         

ERROR_TYPE_DOMINANT = 1.5  

CONCENTRATION = 50        
SPREAD_TOPICS = 3        

CF_PER_OCCURRENCE = 0.4    
CF_CONFIRMED = 0.8        
CF_LIKELY = 0.5         

LOW_SCORE_GAP = 30      
PERFECT_SCORE = 100       
FEW_ERRORS_RATIO = 0.1   

```

---

### <a id="📄-kbs-engine-py"></a>📄 `kbs/engine.py`

**File Info:**
- **Size**: 18.31 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/engine.py`
- **Relative Path**: `kbs`
- **Created**: 2026-07-04 08:27:49 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:56:50 (America/Los_Angeles / GMT-07:00)
- **MD5**: `752ca65f8f5da307b9832e44132f8ca5`
- **SHA256**: `dbf0be5fe770d3155543fc2aac3533a2232c0e7c2e7ecc8f28a1569b2389eb18`
- **Encoding**: UTF-8

**File code content:**

```python
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

```

---

### <a id="📄-kbs-explain-py"></a>📄 `kbs/explain.py`

**File Info:**
- **Size**: 2.04 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/explain.py`
- **Relative Path**: `kbs`
- **Created**: 2026-06-28 17:38:23 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:57:18 (America/Los_Angeles / GMT-07:00)
- **MD5**: `d215ed5ecfe3cc9ef6feccdad9d1040a`
- **SHA256**: `eaaf8a3de344d8e230d88b13c9d0bc39e371454ac2737cca87527da16122404e`
- **Encoding**: UTF-8

**File code content:**

```python
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

```

---

### <a id="📄-kbs-facts-py"></a>📄 `kbs/facts.py`

**File Info:**
- **Size**: 3.83 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/facts.py`
- **Relative Path**: `kbs`
- **Created**: 2026-07-04 08:19:01 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:58:04 (America/Los_Angeles / GMT-07:00)
- **MD5**: `016b7b26a28a7f185474ebaf76bd9236`
- **SHA256**: `f61a7b3c8cf0cf6d7d1a0bdc48ec6dcd0778aebd8ba8febf4a9fff0e560cddfd`
- **Encoding**: UTF-8

**File code content:**

```python
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

```

---

### <a id="📄-kbs-interpret-py"></a>📄 `kbs/interpret.py`

**File Info:**
- **Size**: 3.92 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/interpret.py`
- **Relative Path**: `kbs`
- **Created**: 2026-07-04 08:19:09 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-13 10:59:00 (America/Los_Angeles / GMT-07:00)
- **MD5**: `87d8685228b10d2e06c737bdcb250a69`
- **SHA256**: `7e36a338993ba4190e7699843ca6afdd9c16a11ad0e9b51a92ac4e92191b55ad`
- **Encoding**: UTF-8

**File code content:**

```python
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

```

---

### <a id="📄-kbs-report-generator-py"></a>📄 `kbs/report_generator.py`

**File Info:**
- **Size**: 8.94 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `kbs/report_generator.py`
- **Relative Path**: `kbs`
- **Created**: 2026-07-04 15:22:13 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 07:09:44 (America/Los_Angeles / GMT-07:00)
- **MD5**: `01e20ef89eb2d3abe74c40b857813d75`
- **SHA256**: `4d488d5ea625c1b08ef0b7ebe086d70d9133e1e1731ed8e236957c0258ed9c88`
- **Encoding**: UTF-8

**File code content:**

```python
import io
from datetime import datetime

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

FONT = "Arial"
GREEN = RGBColor(0x1B, 0x6B, 0x3A)      

_STATUS_AR = {"confirmed": "مؤكَّد", "likely": "مرجَّح", "weak": "ضعيف"}
_PRIORITY_AR = {"critical": "حرجة", "high": "عالية", "medium": "متوسطة", "low": "منخفضة"}
_ERR_KIND_AR = {
    "conceptual": "خلل فهمي",
    "procedural": "خلل تطبيقي",
    "mixed": "مختلط (فهمي وتطبيقي)",
    "careless": "زلّات (إهمال)",
}


# ══════════════════════════════════════════════════════════════ #
#                       أدوات التنسيق (RTL + Arial)             #
# ══════════════════════════════════════════════════════════════ #
def _apply_font(run, size, bold, color):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.rtl = True
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.get_or_add_rFonts()
    rfonts.set(qn("w:ascii"), FONT)
    rfonts.set(qn("w:hAnsi"), FONT)
    rfonts.set(qn("w:cs"), FONT)


def _rtl_paragraph(paragraph, align=WD_ALIGN_PARAGRAPH.RIGHT):
    pPr = paragraph._p.get_or_add_pPr()
    pPr.append(OxmlElement("w:bidi"))
    paragraph.alignment = align


def _add_para(container, text, size=11, bold=False, color=None,
              align=WD_ALIGN_PARAGRAPH.RIGHT):
    p = container.add_paragraph()
    _rtl_paragraph(p, align)
    _apply_font(p.add_run(text), size, bold, color)
    return p


def _fill_cell(cell, text, bold=False, color=None, size=10):
    cell.text = ""
    p = cell.paragraphs[0]
    _rtl_paragraph(p)
    _apply_font(p.add_run(str(text)), size, bold, color)


def _new_table(doc, headers):
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    table._tbl.tblPr.append(OxmlElement("w:bidiVisual"))   # جدول RTL
    for cell, head in zip(table.rows[0].cells, headers):
        _fill_cell(cell, head, bold=True, color=GREEN)
    return table


# ══════════════════════════════════════════════════════════════ #
#                       اشتقاق نوع الخلل                        #
# ══════════════════════════════════════════════════════════════ #
def _error_kind(topic, diag_by_topic):
    """نوع الخلل من التشخيص، أو احتياطياً من عدّادات الموضوع."""
    kind = diag_by_topic.get(topic["topic_id"])
    if kind in _ERR_KIND_AR:
        return _ERR_KIND_AR[kind]
    c = topic.get("conceptual_errors", 0)
    a = topic.get("application_errors", 0)
    k = topic.get("careless_errors", 0)
    if c + a + k == 0:
        return "—"
    if k > c + a:
        return _ERR_KIND_AR["careless"]
    if c > a:
        return _ERR_KIND_AR["conceptual"]
    if a > c:
        return _ERR_KIND_AR["procedural"]
    return _ERR_KIND_AR["mixed"]


# ══════════════════════════════════════════════════════════════ #
#                       الدالة الرئيسية                         #
# ══════════════════════════════════════════════════════════════ #
def generate_report(result: dict, output_path: str = None) -> bytes:
    """تبني تقرير .docx من ناتج interpret() وتُرجع محتواه bytes.

    إن مُرّر output_path حُفظ الملف هناك أيضاً. تعمل مع أي نتيجة حتى الخالية.
    """
    doc = Document()

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(11)
    _rfonts = normal.element.get_or_add_rPr().get_or_add_rFonts()
    _rfonts.set(qn("w:ascii"), FONT)
    _rfonts.set(qn("w:hAnsi"), FONT)
    _rfonts.set(qn("w:cs"), FONT)

    student_id = result.get("student_id") or "—"
    quiz_id = result.get("quiz_id") or "—"

    # ── العنوان ──────────────────────────────────────────── #
    _add_para(doc, "تقرير أداء الطالب", size=20, bold=True, color=GREEN,
              align=WD_ALIGN_PARAGRAPH.CENTER)
    _add_para(doc, f"الطالب: {student_id}  —  الاختبار: {quiz_id}",
              size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)

    # ── المستوى والنتيجة ─────────────────────────────────── #
    _add_para(doc, "الملخّص العام", size=15, bold=True, color=GREEN)
    _add_para(doc, f"المستوى العام: {result.get('level') or '—'}", size=12, bold=True)
    _add_para(doc, f"النتيجة المئوية: {result.get('score', 0)}%", size=12, bold=True)

    # ── نقاط القوة ───────────────────────────────────────── #
    _add_para(doc, "نقاط القوة", size=15, bold=True, color=GREEN)
    strengths = result.get("strengths", [])
    if strengths:
        table = _new_table(doc, ["الموضوع", "الدقة %"])
        for t in strengths:
            row = table.add_row().cells
            _fill_cell(row[0], t["topic_name"])
            _fill_cell(row[1], f"{t['accuracy']}%")
    else:
        _add_para(doc, "لا توجد نقاط قوة مسجّلة.", size=11)

    # ── نقاط الضعف ───────────────────────────────────────── #
    _add_para(doc, "نقاط الضعف", size=15, bold=True, color=GREEN)
    weaknesses = result.get("weaknesses", [])
    if weaknesses:
        diag_by_topic = {}
        for d in result.get("_diagnoses", []):
            if d["kind"] in _ERR_KIND_AR:
                diag_by_topic[d["topic"]] = d["kind"]
        table = _new_table(doc, ["الموضوع", "الدقة %", "نوع الخلل"])
        for t in weaknesses:
            row = table.add_row().cells
            _fill_cell(row[0], t["topic_name"])
            _fill_cell(row[1], f"{t['accuracy']}%")
            _fill_cell(row[2], _error_kind(t, diag_by_topic))
    else:
        _add_para(doc, "لا توجد نقاط ضعف مسجّلة.", size=11)

    # ── المفاهيم الخاطئة المكتشفة ────────────────────────── #
    misconceptions = result.get("misconceptions", [])
    if misconceptions:
        _add_para(doc, "المفاهيم الخاطئة المكتشفة", size=15, bold=True, color=GREEN)
        table = _new_table(doc, ["المفهوم الخاطئ", "الحالة", "الثقة", "الأسئلة الشاهدة"])
        for m in misconceptions:
            row = table.add_row().cells
            _fill_cell(row[0], m["label"])
            _fill_cell(row[1], _STATUS_AR.get(m["status"], m["status"]))
            _fill_cell(row[2], m["cf"])
            _fill_cell(row[3], "، ".join(m.get("occurrences", [])) or "—")

    # ── التوصيات ─────────────────────────────────────────── #
    _add_para(doc, "التوصيات الدراسية", size=15, bold=True, color=GREEN)
    recommendations = result.get("recommendations", [])
    if recommendations:
        for r in recommendations:
            prio = _PRIORITY_AR.get(r["priority"], r["priority"])
            _add_para(doc, f"[{prio}] {r['message']}", size=12, bold=True)
            _add_para(doc, f"↳ {r['explanation']}", size=11)
    else:
        _add_para(doc, "لا توجد توصيات.", size=11)

    # ── تاريخ الإنشاء ────────────────────────────────────── #
    doc.add_paragraph()
    _add_para(doc, f"تاريخ إنشاء التقرير: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
              size=9, color=RGBColor(0x77, 0x77, 0x77))

    # ── الإخراج ──────────────────────────────────────────── #
    buffer = io.BytesIO()
    doc.save(buffer)
    data = buffer.getvalue()
    if output_path:
        with open(output_path, "wb") as f:
            f.write(data)
    return data

```

---

### <a id="📄-tests-test-kbs-py"></a>📄 `tests/test_kbs.py`

**File Info:**
- **Size**: 4.95 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `tests/test_kbs.py`
- **Relative Path**: `tests`
- **Created**: 2026-06-28 17:38:23 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:56:56 (America/Los_Angeles / GMT-07:00)
- **MD5**: `5128462209231248efd9711e2756537d`
- **SHA256**: `730559f045cd6df0122ceb872709f9c722ef2ba39abb28fdc951f999641a5b10`
- **Encoding**: UTF-8

**File code content:**

```python
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
```

---

### <a id="📄-dashboard-py"></a>📄 `dashboard.py`

**File Info:**
- **Size**: 9.95 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `dashboard.py`
- **Relative Path**: `root`
- **Created**: 2026-07-04 15:23:01 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-06 06:20:22 (America/Los_Angeles / GMT-07:00)
- **MD5**: `feb1f280ff8f033885ff4b7c680216f2`
- **SHA256**: `e1bdf367042cb7afc0ba7efff5ca8cf5a2729ad0feb83ae72f13a8876b00af72`
- **Encoding**: UTF-8

**File code content:**

```python
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

```

---

### <a id="📄-demo-py"></a>📄 `demo.py`

**File Info:**
- **Size**: 1.91 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `demo.py`
- **Relative Path**: `root`
- **Created**: 2026-06-28 17:38:23 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-06-28 18:09:49 (America/Los_Angeles / GMT-07:00)
- **MD5**: `b08a67b7ff5441a44eb7e54f3bcd41c4`
- **SHA256**: `504f150d87bf0a9a9af3c915946f295081c728baccc13789bf082ea2a9874cf6`
- **Encoding**: UTF-8

**File code content:**

```python
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

```

---

### <a id="📄-integration-md"></a>📄 `INTEGRATION.md`

**File Info:**
- **Size**: 6.02 KB
- **Extension**: `.md`
- **Language**: `text`
- **Location**: `INTEGRATION.md`
- **Relative Path**: `root`
- **Created**: 2026-07-04 08:41:49 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-04 08:41:49 (America/Los_Angeles / GMT-07:00)
- **MD5**: `729a4f52d591a08ed9873699aebc107f`
- **SHA256**: `1569977bc0a8985cc63717f5925514db49fdb69ae24ff8ef46d0d53ec83d9a0f`
- **Encoding**: UTF-8

**File code content:**

````markdown
# دليل التكامل — KBS Interface Contract

## نظرة عامة

هذا النظام الخبير (KBS) يستقبل إجابات الطالب ويُنتج تشخيصاً 
وتوصيات تعليمية تكيّفية عبر الاستدلال الأمامي (forward chaining) 
مع عوامل اليقين (MYCIN-style certainty factors).

## Input Contract

### الصيغة المطلوبة (JSON)

~~~~json
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
~~~~

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

~~~~bash
python demo.py              # تشغيل تفاعلي
python -m tests.test_kbs    # تشغيل الاختبارات
~~~~

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
````

---

### <a id="📄-readme-md"></a>📄 `README.md`

**File Info:**
- **Size**: 5.68 KB
- **Extension**: `.md`
- **Language**: `text`
- **Location**: `README.md`
- **Relative Path**: `root`
- **Created**: 2026-07-04 08:42:25 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-04 08:42:25 (America/Los_Angeles / GMT-07:00)
- **MD5**: `74b26debc19fe217701ab7d3ae33e95a`
- **SHA256**: `44e01b31c17f1f271f389787b951302e487316ecda6a630e09bf93e503c69ea1`
- **Encoding**: UTF-8

**File code content:**

````markdown
# النظام الخبير لتفسير أداء الطالب (KBS)

نظام خبير قائم على القواعد (Experta) يأخذ **إجابات الطالب الخام** فيشخّص مستواه،
ويكتشف **المفاهيم الخاطئة** المحددة في ذهنه بعوامل يقين، ويولّد **توصيات دراسية
مع تفسير لكل توصية**، مع مرفق **Why/How** يفسّر سلسلة استدلاله.

مشروع مستقل لمادة نظم قواعد المعرفة، مصمَّم ليُدمج لاحقاً في المنصة التعليمية.

---

## الالتزام بفلسفة Experta

النظام مكتوب وفق الأسلوب الذي اعتمدته المحاضرات — لا منطق إجرائي داخل القواعد:

- **لا حلقات `for`/`while` داخل القواعد:** العدّ وتجميع عوامل اليقين يتمّان بإطلاق
  القاعدة مرّةً لكل حقيقة في الذاكرة العاملة (مطابقة الأنماط بديل الحلقة).
- **لا `if/elif` لتوجيه التدفّق:** كل فرع منطقي قاعدة مستقلة، والتمييز يتم عبر
  أنماط القسم الأيسر و`TEST`/`P()`.
- **كل الحالة في الذاكرة العاملة:** الإحصاءات والتشخيصات واليقين والتوصيات كلها
  حقائق (`declare`/`modify`)، لا متغيّرات بايثون.
- **الترتيب يُدار بالأجندة و`salience`** لفض النزاع، لا بترتيب الأسطر.

الحلقات الوحيدة في المشروع هي عند حدّ الإدخال/الإخراج فقط (تهيئة الحقائق من JSON،
ثم قراءة النتيجة من الذاكرة العاملة) — خارج القواعد تماماً.

---

## التشغيل

~~~~bash
pip install -r requirements.txt        # انظري ملاحظة frozendict في الملف
python demo.py                         # عرض كامل في سطر الأوامر
python tests/test_kbs.py               # الاختبارات
streamlit run dashboard.py             # لوحة التحكم التفاعلية
~~~~

> تحتوي لوحة التحكم على مُحدِّد سيناريوهات في الأعلى يتيح اختيار أحد الطلاب
> الجاهزين (عام / أساسيات تعلّم الآلة / قواعد البيانات / طالب متفوق) من
> `data/scenarios/`، أو رفع ملف JSON خاص بكِ.

> **ملاحظة بيئة:** `experta` يثبّت `frozendict==1.2` القديم الذي يفشل على Python 3.10+
> بخطأ `collections.Mapping`. إذا رفض pip التثبيت بسبب التعارض:
> ~~~~bash
> pip install experta PyYAML streamlit
> pip install frozendict==2.4.7 --no-deps
> ~~~~

---

## المعمارية (الوحدات)

| الوحدة | الدور |
|---|---|
| `config.py` | كل العتبات في مكان واحد (ضبط الحساسية) |
| `catalog.yaml` + `catalog.py` | كتالوج المفاهيم الخاطئة — أصل المعرفة |
| `certainty.py` | تعبير دمج عوامل اليقين (MYCIN) المستخدَم داخل قاعدة التجميع |
| `facts.py` | حقائق الذاكرة العاملة (كل حالة النظام) |
| `engine.py` | كل القواعد: العدّ، اليقين، التشخيص، التوصيات |
| `explain.py` | مرفق Why/How |
| `interpret.py` | الواجهة العامة: `interpret(attempt) → result` |
| `dashboard.py` | لوحة التحكم التفاعلية (Streamlit) |

تدفّق الاستدلال داخل المحرك (بالـ salience):
تهيئة العدّادات → عدّ الإجابات وتجميع اليقين → إنهاء كل موضوع وتثبيت حالة اليقين →
بناء المقاييس العامة → تصنيف المواضيع → تحديد نوع الخلل → التوزّع → الحالات الخاصة →
توليد التوصيات. ثم يُقرأ كل ذلك من الذاكرة العاملة لبناء المخرج.

---

## المدخل والمخرج (عقد التكامل)

**المدخل** — وقائع كل سؤال (من وحدتي توليد الأسئلة والتصحيح):

~~~~json
{"question_id": "q3", "topic_id": "ch3_normalization",
 "selected_option": "B", "correct_option": "A", "is_correct": false,
 "selected_misconception": "concept_confusion",
 "misconception_detail": "خلط بين الاعتماد على شكل الجدول وتحليل الاعتماديات"}
~~~~

> حقل `misconception_detail` **اختياري** (افتراضيه `""`، متوافق خلفياً): يعرض
> السياق المحدّد للخطأ فيظهر في نهاية رسالة التوصية بالصيغة
> `تصحيح: <الوصف العام> — <السياق المحدّد>`.

**المخرج** — المستوى، القوة/الضعف، المفاهيم الخاطئة بثقتها، والتوصيات مع تفسيرها.
نقطة التكامل الوحيدة مع المنصة هي الدالة `interpret(attempt)`؛ تُغلَّف لاحقاً بـ API.

---

## التوسيع

- **إضافة موضوع/مفهوم خاطئ:** عدّلي `catalog.yaml` فقط.
- **ضبط الحساسية:** عدّلي العتبات في `config.py` دون لمس القواعد.
- **إضافة قاعدة:** أضيفي `@Rule` جديدة في `engine.py`.
- **قيم `selected_misconception` المقبولة:** `conceptual_error` | `surface_association` | `concept_confusion` | `careless` | `none`
- **سياق محدّد للأخطاء:** أضيفي حقل `misconception_detail` (اختياري) لكل سؤال خاطئ
  ذي مفهوم `conceptual`/`procedural` ليظهر في رسالة التوصية.

````

---

### <a id="📄-requirements-txt"></a>📄 `requirements.txt`

**File Info:**
- **Size**: 271 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `requirements.txt`
- **Relative Path**: `root`
- **Created**: 2026-07-04 15:22:27 (America/Los_Angeles / GMT-07:00)
- **Modified**: 2026-07-04 15:22:27 (America/Los_Angeles / GMT-07:00)
- **MD5**: `5b31c96a9d36eb15671527fdf826612b`
- **SHA256**: `3e5dda0f1a2aafc86b8b557eb1eb69c390e8bf307eef57f5f19efc73cd883452`
- **Encoding**: UTF-8

**File code content:**

```text
# التثبيت: إذا رفض pip بسبب تعارض frozendict، ثبّتي كل مكتبة وحدها:
#   pip install experta PyYAML streamlit
#   pip install frozendict==2.4.7 --no-deps
experta==1.9.4
frozendict>=2.4.4
PyYAML>=6.0
streamlit>=1.30
python-docx>=1.1

```

---

