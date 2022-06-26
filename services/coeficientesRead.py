import json

def jsonRead(caminho:json) -> dict:
    """faz a leitura de um arquivo json
    Args:
        caminho (path): local do arquivo json
    Return:
        dict
    """
    with open(caminho,"r") as tabela:
        tabelaCoeficientes = json.load(tabela)
        
    return(tabelaCoeficientes)