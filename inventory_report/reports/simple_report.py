from datetime import datetime
import math


class SimpleReport:
    @classmethod
    def _get_diff_date(cls, date_product: str) -> int:
        """
        Método privado da classe SimpleReport para ser usado no método 'sort'.
        Calcula a diferença em dias de uma data de teste com a data atual.
        Retorna infinito caso a diferença seja menor que zero.

        Entrada:
        --------

        date_product: str
            data de teste no formato string 'YYYY-MM-DD'

        Saída:
        ------

        days: int
            a diferença em dias data de teste com a data atual
            ou 'infinito' casa a diferença seja menor que zero
        """
        now = datetime.now()
        this_date = datetime.fromisoformat(date_product)
        diff = (this_date - now).days
        if diff < 0:
            return math.inf
        return diff

    @classmethod
    def _get_number_products_per_company(cls, products: list) -> list:
        """
        Método privado da classe SimpleReport para ser usado pelo método
        'generate' da mesma classe.
        Retorna uma lista não ordenada de dicionários contendo o nome da
        empresa e sua respectiva quantidade de produtos

        Entrada:
        --------

        products: list[dict]
            lista com os dicionário de cada produto

        Saída:
        ------

        number_products_per_company: list[dict]
            lista de dicionários {"name": NOME_DA_EMPRESA, "qtd": QTD_PRODUTOS}
        """
        companies = [product["nome_da_empresa"] for product in products]
        companies_list = dict.fromkeys(companies, 0)

        for company_name in companies_list.keys():
            companies_list[company_name] = companies.count(company_name)

        companies_list = [
            {"name": k, "qtd": v} for (k, v) in companies_list.items()
        ]

        return companies_list

    @classmethod
    def generate(cls, products: list) -> str:
        """
        Método público da classe SimpleReport para gerar um relatório simples.

        Entrada:
        --------

        products: list[dict]
            lista com os dicionário de cada produto

        Saída:
        ------

        relatório: str
            Data de fabricação mais antiga: YYYY-MM-DD
            Data de validade mais próxima: YYYY-MM-DD
            Empresa com mais produtos: NOME_DA_EMPRESA
        """

        products_list = products.copy()

        products_list.sort(key=lambda product: product["data_de_fabricacao"])

        oldest_product = products_list[0].get("data_de_fabricacao")

        products_list.sort(
            key=lambda product: SimpleReport._get_diff_date(
                product["data_de_validade"]
            )
        )

        closest_validity_product = products_list[0].get("data_de_validade")

        number_products_per_company = (
            SimpleReport._get_number_products_per_company(products)
        )

        number_products_per_company.sort(
            key=lambda company: company["qtd"],
            reverse=True,
        )

        most_counted_company = number_products_per_company[0]["name"]

        return str(
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_validity_product}\n"
            f"Empresa com mais produtos: {most_counted_company}"
        )
