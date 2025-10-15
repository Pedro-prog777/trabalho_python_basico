# Questão 4 - Verificar se a pessoa é maior ou menor de idade

def verificar_idade(idade):
    """
    Recebe a idade de uma pessoa e retorna se ela é
    maior ou menor de idade.
    """
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
