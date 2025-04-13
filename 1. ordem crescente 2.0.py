#Apos uma observação durando a realização da questão 10, percebi que poderia tornar o codigo de ordem crescente mais pratico, podendo escrever os 3 numeros em uma unica linha
numeros = list(map(int, input("Digite três números separados por espaço: ").split())) # Solicita três números inteiros em uma única linha, separados por espaço
for i in range(3): # Verifica se foram digitados exatamente três números
    if len(numeros) != 3:
        print("Por favor, digite exatamente três números.")
        exit()
numeros.sort() # Ordena os números em ordem crescente

print("Os números em ordem crescente são:", numeros) # Exibe os números em ordem crescente
