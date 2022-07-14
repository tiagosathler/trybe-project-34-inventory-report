from datetime import date
from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        23,
        "Xablau",
        "Interesting Inc.",
        date(2020, 11, 13),
        date(2022, 7, 15),
        "x003",
        "Ipsulumloremem",
    )
    assert product.id == 23
    assert product.nome_do_produto == "Xablau"
    assert product.nome_da_empresa == "Interesting Inc."
    assert product.data_de_fabricacao == "2020-11-13"
    assert product.data_de_validade == "2022-07-15"
    assert product.numero_de_serie == "x003"
    assert product.instrucoes_de_armazenamento == "Ipsulumloremem"
