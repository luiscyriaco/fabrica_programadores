# Programa para registrar nome e e-mail em um arquivo texto

# Solicita ao usuário que insira seu nome e e-mail
nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

# Abre (ou cria) o arquivo 'pessoa.txt' no modo de anexação ('a')
arquivo = open("pessoa.txt", "a") # Modo 'a' para anexar ao arquivo existente
arquivo.write(nome + "|" + "\n") # Escreve o nome no arquivo seguido de uma nova linha
arquivo.close() # Fecha o arquivo após a escrita