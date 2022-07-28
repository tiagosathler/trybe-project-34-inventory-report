import xml.etree.ElementTree as ElementTree
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, filename: str) -> list:
        if "xml" not in filename.lower():
            raise ValueError("Arquivo inválido")

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
