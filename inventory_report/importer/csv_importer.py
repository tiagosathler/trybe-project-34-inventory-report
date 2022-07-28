import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, filename: str) -> list:
        if "csv" not in filename.lower():
            raise ValueError("Arquivo inválido")

        with open(filename, "r", encoding="utf-8") as file:
            return list(csv.DictReader(file, delimiter=",", quotechar='"'))
