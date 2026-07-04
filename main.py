from dataclasses import dataclass

@dataclass
class Empresa:
    nome: str
    problema: str
    score: int # Troquei de float para int porque as notas vao de 1 a 5 somente


def mostrar_menu():
    print("\n----MENU----")
    print("1. Registrar nova base de dados")
    print("2. Consultar uma empresa/produto")
    print("3. Excluir uma avaliação?")
    print("4. Encerrar o programa")
    opcao = input("Escolha uma opção (1-4): ")
    return opcao


def menu():
    # Melhorar essa funcao se possivel, tratando erros
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
        empresas = []
        # Leitura nativa do python
        with open(path_csv, "r", encoding="utf-8") as file:
            cabecalho = file.readline()
            for linha in file:
                dados = linha.strip().split(";")
                if len(dados) >= 3:
                    try:
                        nova_empresa = Empresa(nome=dados[0], problema=dados[1], score=dados[2])
                        empresas.append(nova_empresa)
                        # Vou colocar outra coisa aqui futuramente, coloquei uma lista primeiro para testar
                        # minha_arvore.append(nova_empresa)...
                    except ValueError:
                        continue # Ignora se por algum acaso vier algum lixo que nao seja numero
        
        print(f"{len(empresas)} registros carregados na memoria")
        return empresas
    except FileNotFoundError:
        print("Arquivo nao existe, verifique o caminho")
        return None 

if __name__ == "__main__":
    menu()