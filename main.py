import pandas as pd
from dataclasses import dataclass

@dataclass
class Empresa:
    nome: str
    score: float


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
            path = input("Digite o caminho EXATO para o documento: ")
            carregar_arquivo(path)
        elif escolha == '2':
            print("Função Consulta")
        elif escolha == '3': 
            print("Função Excluir")
        elif escolha == '4':
            print("Encerrando o programa")
            break
        else:
            print("Opção inválida! Tente novamente")
def carregar_arquivo(path_csv: str):
    try:
        df = pd.read_csv(path_csv)
    except FileNotFoundError:
        print("Arquivo não existe, verifique o caminho")
        return []
    #Nesse momento coletar os dados e organizar utilizando o pandas. OBS.: Não comecei pq to sem os arquivos csv para ver como está organizado
menu()