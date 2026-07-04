def mostrar_menu():
    print("\n----MENU----")
    print("1. Registrar nova base de dados")
    print("2. Consultar uma empresa/produto")
    print("3. Excluir uma avaliação?")
    print("4. Encerrar o programa")
    opcao = input("Escolha uma opção (1-4): ")
    return opcao


def menu():
    while(True):
        escolha = mostrar_menu()

        if escolha == '1':
            print("Função Registrar")
        elif escolha == '2':
            print("Função Consulta")
        elif escolha == '3': 
            print("Função Excluir")
        elif escolha == '4':
            print("Encerrando o programa")
            break
        else:
            print("Opção inválida! Tente novamente")

menu()