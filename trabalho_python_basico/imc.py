# Questão 5 - Cálculo e classificação do IMC
def calcular_imc(peso, altura):
    """Calcula o IMC de uma pessoa."""
    imc = peso / (altura ** 2)
    return imc


def classificar_imc(imc):
    """Classifica o IMC de acordo com a faixa de peso."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc <= 24.9:
        return "Peso normal"
    else:
        return "Acima do peso"
meu_imc = calcular_imc(70, 1.75)
print(f"IMC: {meu_imc:.2f}")                
print(classificar_imc(meu_imc))             

