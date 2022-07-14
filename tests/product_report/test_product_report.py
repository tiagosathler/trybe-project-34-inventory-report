from inventory_report.inventory.product import Product
from datetime import date


def test_relatorio_produto():
    product = Product(
        23,
        "Xablau",
        "Interesting Inc.",
        date(2020, 11, 13),
        date(2022, 7, 15),
        "x003",
        "Ipsulumloremem",
    )

    expected = str(
        "O produto Xablau"
        " fabricado em 2020-11-13"
        " por Interesting Inc. com validade"
        " até 2022-07-15"
        " precisa ser armazenado Ipsulumloremem."
    )

    assert repr(product) == expected
