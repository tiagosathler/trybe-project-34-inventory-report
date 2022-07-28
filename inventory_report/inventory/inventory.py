from abc import ABC, abstractmethod
import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class OpenWithStrategy(ABC):
    @classmethod
    @abstractmethod
    def _open_file(cls, filename: str) -> list:
        raise NotImplementedError


class OpenWithCsv(OpenWithStrategy):
    @classmethod
    def _open_file(cls, filename: str) -> list:
        with open(filename, 'r', encoding='utf-8') as file:
            return list(csv.DictReader(file, delimiter=',', quotechar='"'))


class Inventory:
    @classmethod
    def _open_file_with(cls, filename: str) -> list:
        if 'csv' in filename.lower():
            return OpenWithCsv._open_file(filename)

    @classmethod
    def import_data(cls, filename: str, report: str) -> str:
        list_products = Inventory._open_file_with(filename)
        if (report.lower() == 'simples'):
            simple_report = SimpleReport.generate(list_products)
            return simple_report
        elif (report.lower() == 'completo'):
            return CompleteReport.generate(list_products)
        else:
            return ""
