
# Solicita a string e os caracteres
string = input("Digite uma palavra: ")

if len(string) >= 100: # verifica se a string tem 100 ou mais caracteres
    print ("Digite uma palavra com menos de 100 caracteres!") # imprime a mensagem de erro
    exit() # encerra o programa

caracter1 = input("Digite o primeiro caracter (a ser substituído): ")
caracter2 = input("Digite o segundo caracter (substituto): ")

# Substitui todas as ocorrências do primeiro caracter pelo segundo
string_resultante = string.replace(caracter1, caracter2)

# Exibe a string resultante
print("String resultante:", string_resultante)