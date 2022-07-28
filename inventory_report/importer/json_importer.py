import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, filename: str) -> list:
        if "json" not in filename.lower():
            raise ValueError("Arquivo inválido")

        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
