# Solicita os dois valores X e Y
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

menor = min(x, y) # Define qual é o menor valor
maior = max(x, y) # Define qual é o maior valor

for numero in range(menor + 1, maior): # Loop entre os números de X e Y

    # Verifica se o número tem resto 2 ou 3 quando dividido por 5
    if numero % 5 == 2:
    elif numero % 5 == 3: 

        print(numero) # Imprime o número os numeros que atendam a esse condição