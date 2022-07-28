from datetime import datetime


class SimpleReport:
    @classmethod
    def _get_diff_date(cls, product: dict) -> int:
        """
        Método desta classe, privado, para ser usado no método 'sort'.
        Calcula a diferença em segundos da data atual com a data de
        fabricação de um produto.

        Entrada:
        --------

        product: dict
            dicionário produto com a chave 'data_de_validade'

        Saída:
        ------

        seconds: int
            a diferença em segundos da 'data_de_validade' com a data atual
        """
        now = datetime.now()
        this_date = datetime.fromisoformat(product["data_de_validade"])
        diff = this_date - now
        return diff.seconds

    @classmethod
    def _get_most_counted_company(cls, products: list) -> str:
        """
        Método desta classe, privado, para ser usado pelo método 'generate'
        da mesma classe.
        Encontra o nome da empresa mais repetida na lista de dicionários de
        produtos.

        Entrada:
        --------

        products: list[dict]
            lista com os dicionário de cada produto

        Saída:
        ------

        most_counted_company: str
            o nome da empresa mais repetida na lista de dicionários de produtos
        """
        companies = [product["nome_da_empresa"] for product in products]
        companies_list = dict.fromkeys(companies, 0)

        for company_name in companies_list.keys():
            companies_list[company_name] = companies.count(company_name)

        companies_list = [
            {"name": k, "count": v} for (k, v) in companies_list.items()
        ]

        companies_list.sort(
            key=lambda company: company["count"],
            reverse=True,
        )

        return companies_list[0]["name"]

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

        products.sort(key=lambda product: product["data_de_fabricacao"])

        oldest_product = products[0].get("data_de_fabricacao")

        products.sort(key=SimpleReport._get_diff_date)

        closest_validity_product = products[0].get("data_de_validade")

        most_counted_company = SimpleReport._get_most_counted_company(products)

        return str(
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_validity_product}\n"
            f"Empresa com mais produtos: {most_counted_company}"
        )
