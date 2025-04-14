numero = int(input("Digite um número: ")) # Solicita um número ao usuário

if numero < 2: # Verifica se o número se encaixa na exceção do 1 e 0
    print("Número não é Primo")
else:
    primo = True
    for i in range(2, int(numero ** 1/2) + 1): # Verifica se o número é divisível por algum número entre 2 e a raiz quadrada do número
        if numero % i == 0: # se o número for divisível, não é primo
            primo = False 
            break # Sai do loop se encontrar um divisor
    if primo:
        print("Número Primo")
    else:
        print("Número não Primo")
