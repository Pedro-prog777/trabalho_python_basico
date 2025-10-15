# try.py

# QUESTÃO 1 - Divisão com tratamento de erro de divisão por zero

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = numero1 / numero2
    print(f"Resultado da divisão: {resultado}")

except ZeroDivisionError:
    print(" Erro: Não é possível dividir por zero. Tente novamente.")



# QUESTÃO 2 - Tratando erro ao digitar algo que não seja número

try:
    numero = float(input("\nDigite um número: "))
    print(f"Você digitou o número {numero}")

except ValueError:
    print(" Erro: Você digitou um texto em vez de um número. Por favor, tente novamente.")


# QUESTÃO 3 - Código com dois tipos de erro diferentes

try:
    valor = float(input("\nDigite um número para dividir: "))
    divisor = float(input("Digite o divisor: "))
    resultado = valor / divisor
    print(f"Resultado: {resultado}")

except ValueError:
    print(" Erro: Você digitou algo que não é um número válido.")
except ZeroDivisionError:
    print(" Erro: Não é possível dividir por zero.")
except Exception as erro:
    print(f" Ocorreu um erro inesperado: {erro}")



# QUESTÃO 4 - Função dividir(a, b) com tratamento de erro

def dividir(a, b):
    """
    Função que divide dois números e trata erro de divisão por zero.

    Parâmetros:
        a (float): numerador
        b (float): denominador

    Retorno:
        float: resultado da divisão, se possível.
        str: mensagem de erro, caso a divisão não seja válida.
    """
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return " Erro: Divisão por zero não é permitida."


print("\n=== Teste da função dividir(a, b) ===")
num1 = float(input("Digite o numerador: "))
num2 = float(input("Digite o denominador: "))

resultado_funcao = dividir(num1, num2)
print("Resultado:", resultado_funcao)
