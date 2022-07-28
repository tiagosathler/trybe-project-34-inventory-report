"""
    NOTAS:
        PARTE DO CÓDIGO A SEGUIR SE BASEIA NOS CÓDIGOS DE
        'test_simple_report' e 'factory.py' (classe 'ProductFactory'),
        E FORAM DESENVOLVIDOS PELA TRYBE.
        ELES FORAM USADOS APENAS PARA GERAR OS MOCKS DE PRODUTOS
        E APLICÁ-LOS AO TESTE ESCRITO POR MIM
"""

from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from tests.factories.product_factory import ProductFactory
from faker import Faker
from datetime import datetime, timedelta
import pytest

faker = Faker("pt-BR")

old_date = faker.past_date()
future_date = faker.future_date() + timedelta(days=20)

oldest_date = old_date - timedelta(days=30)
closest_date = datetime.today().date() + timedelta(days=10)
company_bigger_stock = faker.company()


@pytest.fixture
def products():
    return [
        vars(
            ProductFactory(
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock,
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock,
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                data_de_fabricacao=str(oldest_date),
                data_de_validade=str(closest_date),
            )
        ),
    ]


def test_decorar_relatorio(products):
    colored_report = ColoredReport(SimpleReport)
    simple_report = colored_report.generate(products)

    simple_expected_report = (
        "\033[32mData de fabricação mais antiga:\033[0m "
        + f"\033[36m{oldest_date}\033[0m\n"
        + "\033[32mData de validade mais próxima:\033[0m "
        + f"\033[36m{closest_date}\033[0m\n"
        + "\033[32mEmpresa com mais produtos:\033[0m "
        + f"\033[31m{company_bigger_stock}\033[0m"
    )
    # print(f"\nSimple report: \n{simple_report}\n")
    assert simple_expected_report == simple_report

    colored_complete_report = ColoredReport(CompleteReport)
    complete_report = colored_complete_report.generate(products)

    nome_das_empresas = [
        products[0]["nome_da_empresa"],
        company_bigger_stock,
        products[3]["nome_da_empresa"],
    ]

    complete_expected_report = (
        "\033[32mData de fabricação mais antiga:\033[0m "
        + f"\033[36m{oldest_date}\033[0m\n"
        + "\033[32mData de validade mais próxima:\033[0m "
        + f"\033[36m{closest_date}\033[0m\n"
        + "\033[32mEmpresa com mais produtos:\033[0m "
        + f"\033[31m{company_bigger_stock}\033[0m\n"
        + "Produtos estocados por empresa:\n"
        + f"- {nome_das_empresas[0]}: 1\n"
        + f"- {nome_das_empresas[1]}: 2\n"
        + f"- {nome_das_empresas[2]}: 1\n"
    )
    # print(f"\nComplete report: \n{complete_report}\n")
    assert complete_expected_report == complete_report
