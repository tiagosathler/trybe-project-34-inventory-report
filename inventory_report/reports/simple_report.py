from datetime import datetime


def get_diff_date(product: dict) -> int:
    now = datetime.now()
    date = datetime.fromisoformat(product["data_de_validade"])
    return abs(date - now)


def get_most_counted_company(products: list[dict]) -> str:
    companies = [product["nome_da_empresa"] for product in products]
    most_counted_company = ""
    max_count = 0
    for company in companies:
        current_company_count = companies.count(company)
        if current_company_count > max_count:
            most_counted_company = company
            max_count = current_company_count
    return most_counted_company


class SimpleReport:
    @classmethod
    def generate(self, products: list[dict]) -> str:
        """
        Recebe uma lista de dicionários de produtos e retorna
        uma string com a 'Data de fabricação mais antiga',
        a 'Data de validade mais próxima' e
        o nome da 'Empresa com mais produtos'.
        """

        products.sort(key=lambda product: product["data_de_fabricacao"])
        oldest_product = products[0].get("data_de_fabricacao")

        products.sort(key=get_diff_date)
        closest_validity_product = products[0].get("data_de_validade")

        most_counted_company = get_most_counted_company(products)

        return str(
            f"Data de fabricação mais antiga: {oldest_product}\n"
            f"Data de validade mais próxima: {closest_validity_product}\n"
            f"Empresa com mais produtos: {most_counted_company}"
        )
