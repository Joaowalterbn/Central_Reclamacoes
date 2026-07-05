import pandas as pd
caminho1 = r"data/base1.csv"
caminho2 = r"data/baselimpa"

def limpar_base_governo(caminho_entrada, caminho_saida):
    # Le o csv original baixado do governo
    df = pd.read_csv(caminho_entrada, sep=";", encoding="utf-8", on_bad_lines="skip")

    # Filtra apenas as estruturas que importam, coloquei 3 de exemplo, da para extrair mais
    colunas_interesse = ["Tempo Resposta","Nome Fantasia", "Problema", "Nota do Consumidor"]
    df_limpo = df[colunas_interesse].copy()

    # Remove as linhas onde não há nota
    df_limpo = df_limpo[df_limpo["Nota do Consumidor"] != "Não Avaliada"]
    df_limpo = df_limpo.dropna()

    # Salva um arquivo limpo que o programa principal vai ler
    df_limpo.to_csv(caminho_saida, index=False, sep=";")
    print(f"Base de dados limpa e guardada em: {caminho_saida}")

# Rodar isso daqui uma vez somente
limpar_base_governo(caminho1, caminho2)