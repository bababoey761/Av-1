
numeros = list(map(int, input("Digite os numeros separados por espaço: ").split()))

print ("numeros na ordem inversa", numeros[::-1]) # Exibe os números na ordem inversa

numeros.sort(reverse=True)
print ("numeros em ordem decrescente", numeros) # Exibe os números em ordem decrescente