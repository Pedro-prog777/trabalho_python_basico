# Questão 2 - Aplicar desconto de 10%
def aplicar_desconto(preco):
    """Aplica um desconto de 10% sobre o preço informado."""
    desconto = preco * 0.10
    preco_final = preco - desconto
    return preco_final

print(aplicar_desconto(100)) 
