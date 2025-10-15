# funcoes_bolsa.py

def verificar_acao(valor):
    """Verifica se o valor da ação está caro ou barato."""
    if valor > 150.99:
        return "Ação está cara! Compre com cuidado."
    else:
        return "Ação está barata!"
print(verificar_acao(200))
