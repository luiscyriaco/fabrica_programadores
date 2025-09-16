NOME_PROGRAMA = "Agenda de Contatos" # Nome do programa

agenda = [] # lista para armazenar os contatos

# Função para cadastrar um novo contato
def cadastrar_contato(nome):
    agenda.append(nome) # adiciona o contato à agenda
    print(f"Contato '{nome}' cadastrado com sucesso") # confirma o cadastro

# Função para listar todos os contatos
def listar_contatos():
    print("Lista de Contatos: ")   # cabeçalho da lista
    print(agenda) # exibe a lista de contatos
    
# Função para remover um contato
def remover_contato():
    contato_removido = input("Digite o nome do contato a ser removido: ") # solicita o nome do contato a ser removido
    #
    if contato_removido in agenda:
        agenda.remove(contato_removido)
        print(f"Contato '{contato_removido}' removido com sucesso") # confirma a remoção
    else:
        print(f"Contato '{contato_removido}' não encontrado na agenda") # informa que o contato não foi encontrado
        
# Função principal do programa
def main():
    while True:
        print(NOME_PROGRAMA)
        print("-" * 20)
        print("Menu: ") 
        print("1.Cadastrar Contato")
        print("2.Listar Contatos")
        print("3.Remover Contato")
        print("4.Sair")
        print("-" * 20)
        opcao = int(input("Escolha uma opção: "))
        
        # Processa a opção escolhida
        if opcao == 1:
            nome = input("Digite um nome para incluir na agenda: ")
            cadastrar_contato(nome)
        elif opcao == 2:
            listar_contatos()
        elif opcao == 3:
            remover_contato()
        elif opcao == 4:
            break
        else:
            print("Opção invalida, tente novamente")
            
            
if __name__ == "__main__": # Executa a função principal
    main()


            
