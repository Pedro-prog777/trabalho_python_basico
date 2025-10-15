# main.py
from funcoes_bolsa import verificar_acao

# Pede ao usuário o valor da ação
valor = float(input("Digite o valor da ação: "))

# Chama a função e mostra o resultado
resultado = verificar_acao(valor)
print(resultado)
from desconto import aplicar_desconto