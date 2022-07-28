from inventory_report.reports.simple_report import SimpleReport
from string import Template


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list) -> str:
        """
        Método público da classe CompleteReport para gerar um relatório
        completo. Herda da classe SimpleReport, modifica-o reaproveitando
        seu método generate para gerar o relatório simples.

        Entrada:
        --------

        products: list[dict]
            lista com os dicionário de cada produto

        Saída:
        ------

        relatório: str
            Data de fabricação mais antiga: YYYY-MM-DD
            Data de validade mais próxima: YYYY-MM-DD
            Empresa com mais produtos: NOME DA EMPRESA
            Produtos estocados por empresa:
            - NOME_DA_EMPRESA_X: QUANTIDADE
            - NOME_DA_EMPRESA_Y: QUANTIDADE
            - NOME_DA_EMPRESA_Z: QUANTIDADE
        """
        simple_report = super().generate(products)
        companies_list = super()._get_number_products_per_company(products)

        t = Template("\n- $name: $qtd")

        companies_list = [
            t.substitute(name=company["name"], qtd=company["qtd"])
            for company in companies_list
        ]

        complete_report = (
            simple_report
            + "\nProdutos estocados por empresa:"
            + "".join(companies_list) + "\n"
        )

        return complete_report
