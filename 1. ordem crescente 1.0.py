# Solicita três números inteiros ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Coloca os números em uma lista e ordena em ordem crescente
numeros = [num1, num2, num3]
numeros.sort()

# Exibe os números em ordem crescente
print("Os números em ordem crescente são:", numeros)