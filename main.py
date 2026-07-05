from dataclasses import dataclass
from hash_table import HashTable, Empresa, Problema, imprimir_ranking

def mostrar_menu():
    print("\n----MENU----")
    print("1. Registrar nova base de dados")
    print("2. Consultar uma empresa/produto")
    print("3. Excluir uma empresa")
    print("4. Exibir ranking das 150 piores empresas")
    print("5. Encerrar o programa")
    opcao = input("Escolha uma opção (1-5): ")
    return opcao


def menu():
    banco_de_dados = None

    ranking = None

    while True:

        escolha = mostrar_menu()

        if escolha == '1':
            path = input("Digite o caminho EXATO para o documento: ")
            resultado = carregar_arquivo(path)
            if resultado is not None:
                banco_de_dados = resultado
        elif escolha == '2':
            if banco_de_dados is None:
                print("\nErro: Carregue a base de dados primeiro.")
            else:
                exibir_consulta(banco_de_dados)
        elif escolha == '3':
            if banco_de_dados is None:
                print("\nErro: Carregue a base de dados primeiro.")
            else:
                if excluir_empresa(banco_de_dados): 
                    ranking = banco_de_dados.ranking()
        elif escolha == '4':
            if banco_de_dados is None:
                print("\nErro: Carregue a base de dados primeiro.")
            else:
                if ranking is None:
                    ranking = banco_de_dados.ranking()
                
                imprimir_ranking(ranking)
        elif escolha == '5':
            print("Encerrando o programa")
            break
        else:
            print("Opção inválida! Tente novamente")


def carregar_arquivo(path_csv: str):
    tabela = HashTable(tamanho=1009)
    registros_lidos = 0
    try:
        with open(path_csv, "r", encoding="utf-8") as file:
            cabecalho = file.readline() # Pula cabecalho

            for linha in file:
                dados = linha.strip().split(";")
                if len(dados) >= 4:
                    try:
                        # Extrai e converte os valores
                        tempo_resposta = float(dados[0])
                        nome_empresa = dados[1].strip()
                        problema = dados[2].strip()
                        nota = float(dados[3])

                        # Cria empresa com os valores1
                        nova_empresa = Empresa(
                            nome=nome_empresa,
                            lista_problemas=[Problema(tipo=problema, quant=1)],
                            acu_nota=nota,
                            cont_nota=1,
                            acu_tempo=tempo_resposta,
                            cont_tempo=1
                        )

                        # Insere nova empresa na tabela
                        tabela.inserir(nova_empresa)
                        registros_lidos += 1
                    except ValueError:
                        continue # Ignora se por algum acaso vier algum lixo que nao seja numero

            print(f"{registros_lidos} reclamacoes indexadas na tabela hash")
            return tabela
                        
    except FileNotFoundError:
        print("Arquivo nao existe, verifique o caminho")
        return None 

def exibir_consulta(banco_de_dados):
    print("\n--- BUSCA DE EMPRESA ---")
    nome_busca = input("Digite o nome exato da empresa:").strip()
    # Chamada o metodo de busca da tabela hash
    empresa_encontrada = banco_de_dados.busca(nome_busca)

    if empresa_encontrada:
        # Calculo das medias
        media_nota = empresa_encontrada.acu_nota / empresa_encontrada.cont_nota
        media_tempo = empresa_encontrada.acu_tempo / empresa_encontrada.cont_tempo

        print(f"\n========================================")
        print(f" RESULTADO PARA: {empresa_encontrada.nome.upper()}")
        print(f"========================================")
        print(f"Total de Reclamações : {empresa_encontrada.cont_nota}")
        print(f"Nota Média do Público: {media_nota:.2f} / 5.00")
        print(f"Tempo Médio Resposta : {media_tempo:.2f} dias")
        print(f"----------------------------------------")
        print(f" PRINCIPAIS PROBLEMAS RELATADOS:")

        problemas_ordenados = sorted(
            empresa_encontrada.lista_problemas,
            key = lambda p: p.quant,
            reverse=True
        )

        for p in problemas_ordenados[:5]:
            print(f" - {p.tipo}: {p.quant} caso(s)")
            print(f"========================================\n")
    else:
        print(f"\nNenhum registro encontrado para a empresa '{nome_busca}'.")

def excluir_empresa(banco_de_dados):
    print("\n--- EXCLUSÃO DE EMPRESA ---")
    nome_remover = input("Digite o nome exato da empresa que deseja excluir: ").strip()

    sucesso = banco_de_dados.excluir(nome_remover)

    if sucesso:
        print(f"\nOs dados da empresa '{nome_remover}' foram excluídos com sucesso do sistema.")
    else:
        print("Erro na exclusao da empresa!")

if __name__ == "__main__":
    menu()