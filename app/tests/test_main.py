import pytest
from app.main import somar, conectar_api

def test_somar_correto():
    assert somar(2, 3) == 5

def test_conectar_api_com_sucesso():
    # O teste passará se o segredo for injetado corretamente pelo GitHub Actions
    assert conectar_api() == "Conexão Estabelecida com Sucesso!"
