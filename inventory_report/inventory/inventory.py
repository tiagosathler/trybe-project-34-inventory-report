from abc import ABC, abstractmethod
import csv
import json
import xml.etree.ElementTree as ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class OpenWithStrategy(ABC):
    @classmethod
    @abstractmethod
    def open_file(cls, filename: str) -> list:
        raise NotImplementedError


class OpenWithCsv(OpenWithStrategy):
    @classmethod
    def open_file(cls, filename: str) -> list:
        with open(filename, "r", encoding="utf-8") as file:
            return list(csv.DictReader(file, delimiter=",", quotechar='"'))


class OpenWithJson(OpenWithStrategy):
    @classmethod
    def open_file(cls, filename: str) -> list:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)


class OpenWithXml(OpenWithStrategy):
    @classmethod
    def open_file(cls, filename: str) -> list:
        with open(filename, "r", encoding="utf-8") as file:
            tree = ElementTree.parse(file)
            root = tree.getroot()

            list_products = [
                {
                    "id": element.find("id").text,
                    "nome_do_produto": element.find("nome_do_produto").text,
                    "nome_da_empresa": element.find("nome_da_empresa").text,
                    "data_de_fabricacao": element.find(
                        "data_de_fabricacao"
                    ).text,
                    "data_de_validade": element.find("data_de_validade").text,
                    "numero_de_serie": element.find("numero_de_serie").text,
                    "instrucoes_de_armazenamento": element.find(
                        "instrucoes_de_armazenamento"
                    ).text,
                }
                for element in root.iterfind("record")
            ]

            return list_products


class Inventory:
    @classmethod
    def _open_file_with(cls, filename: str) -> list:
        if "csv" in filename.lower():
            return OpenWithCsv.open_file(filename)
        elif "json" in filename.lower():
            return OpenWithJson.open_file(filename)
        elif "xml" in filename.lower():
            return OpenWithXml.open_file(filename)
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
