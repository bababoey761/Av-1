n = int(input("Digite o número de alunos: ")) # Lê o número de alunos

if n <= 0:
    print("Número inválido de alunos.") # Verifica se o número de alunos é válido
    exit()
notas = [] # Cria uma lista para armazenar as notas dos alunos
for i in range(n): # loop para Ler as notas dos alunos
    nota = float(input("Digite a nota do aluno {}: ".format(i + 1))) # Lê a nota do aluno
    if nota < 0 or nota > 10: # Verifica se a nota é válida
        print("Nota inválida. As notas devem estar entre 0 e 10.") # Exibe mensagem de erro
        exit()
    notas.append(nota) 

media = sum(notas) / n # Calcula a média das notas 

limite_acima = media * 1.10 # calcula as notas acima de 10% da média
limite_abaixo = media * 0.90 # calcula as notas abaixo de 10% da média

acima = sum(1 for nota in notas if nota > limite_acima) # Conta as notas acima de 10% da média
abaixo = sum(1 for nota in notas if nota < limite_abaixo) # Conta as notas abaixo de 10% da média

# Exibe os resultados
print("media: " f"{media}") # Exibe a média das notas
print("notas acima da media: " f"{acima}")
print("notas abaixo da media: " f"{abaixo}")
