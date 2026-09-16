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
