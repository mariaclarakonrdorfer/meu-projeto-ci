import os

def somar(a, b):

return a + b

def conectar_api():
    # Simulando o consumo de um Secret injetado em memória
    token = os.environ.get("MINHA_API_SECRET")
    if not token:
        raise ValueError("ERRO DE SEGURANÇA: Token não encontrado!")
    return "Conexão Estabelecida com Sucesso!"
