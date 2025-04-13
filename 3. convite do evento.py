
nome = input("Ola! qual seu nome? " ) # pergunta o nome do usuario e armazena a variavel do nome
if len(nome) >= 120: # verifica se o nome tem 120 ou mais caracteres
    print ("Digite um nome com menos de 120 caracteres!") # imprime a mensagem de erro
    exit() # encerra o programa
print (f"seja bem vindo(a),{nome}!" ) # Imprime a mensagem de boas-vindas com o nome inseridojo