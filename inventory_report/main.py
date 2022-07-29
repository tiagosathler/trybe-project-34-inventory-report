import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def args_parser(args: list) -> tuple:
    filename = None
    report_method = None
    if len(args) == 3:
        filename = args[1]
        report_method = args[2]
    elif 2 <= len(args) <= 3:
        print("Verifique os argumentos", file=sys.stderr)
        filename = args[0]
        report_method = args[1]
    else:
        raise Exception("Verifique os argumentos")
    return (filename, report_method)


def main() -> None:
    args = sys.argv
    (filename, report_method) = args_parser(args)

    inventory = None

    if "csv" in filename.lower():
        inventory = InventoryRefactor(CsvImporter)
    elif "json" in filename.lower():
        inventory = InventoryRefactor(JsonImporter)
    elif "xml" in filename.lower():
        inventory = InventoryRefactor(XmlImporter)
    else:
        raise ValueError("Unknown file format")

    report = inventory.import_data(filename, report_method)
    print(report, file=sys.stdout, end="")
