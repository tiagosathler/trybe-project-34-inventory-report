from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer_class: Importer):
        self.importer = importer_class
        self.data = []

    def import_data(self, filename: str, report: str) -> str:
        self.data += self.importer.import_data(filename)
        if report.lower() == "simples":
            simple_report = SimpleReport.generate(self.data)
            return simple_report
        elif report.lower() == "completo":
            return CompleteReport.generate(self.data)
        else:
            return ""

    def __iter__(self):
        return InventoryIterator(self.data)

    def __len__(self):
        return len(self.data)
