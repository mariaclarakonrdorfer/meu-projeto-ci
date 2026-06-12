from app.main import somar, conectar_api


def test_somar_correto():
    assert somar(2, 3) == 5


def test_conectar_api_com_sucesso():
    # O teste passa se o segredo for injetado corretamente
    assert conectar_api() == "Conexão Estabelecida com Sucesso!"
