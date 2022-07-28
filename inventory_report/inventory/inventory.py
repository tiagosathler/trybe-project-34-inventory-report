from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @classmethod
    def _open_file_with(cls, filename: str) -> list:
        if "csv" in filename.lower():
            return CsvImporter.import_data(filename)
        elif "json" in filename.lower():
            return JsonImporter.import_data(filename)
        elif "xml" in filename.lower():
            return XmlImporter.import_data(filename)
        else:
            raise ValueError("Unknown filename")

    @classmethod
    def import_data(cls, filename: str, report: str) -> str:
        list_products = Inventory._open_file_with(filename)
        if report.lower() == "simples":
            simple_report = SimpleReport.generate(list_products)
            return simple_report
        elif report.lower() == "completo":
            return CompleteReport.generate(list_products)
        else:
            return ""
