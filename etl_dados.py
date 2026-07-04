import pandas as pd

def limpar_base_governo(caminho_entrada, caminho_saida):
    # Le o csv original baixado do governo
    df = pd.read_csv(caminho_entrada, sep=";", encoding="utf-8", on_bad_lines="skip")

    # Filtra apenas as estruturas que importam, coloquei 3 de exemplo, da para extrair mais
    colunas_interesse = ["Nome fantasia", "Problema", "Nota do consumidor"]
    df_limpo = df[colunas_interesse].copy()

    # Remove as linhas onde não há nota
    df_limpo = df_limpo[df_limpo["Nota do consumidor"] != "Não avaliada"]
    df_limpo.dropna()

    # Salva um arquivo limpo que o programa principal vai ler
    df_limpo.to_csv(caminho_saida, index=False, sep=";")
    print(f"Base de dados limpa e guardada em: {caminho_saida}")

# Rodar isso daqui uma vez somente