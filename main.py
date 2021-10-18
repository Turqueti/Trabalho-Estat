from os import sep
import pandas as pd




if __name__ == "__main__":
    

    arquivo_de_dados_filepath = "./dados/dados-df.csv"
    arquivo_de_teste_filepath = "./dados/dados-menor.csv"
    
    # df = dataFrame
    df = pd.read_csv(arquivo_de_teste_filepath, encoding='ISO-8859-1',sep=';')
    
    # colunas do df
    # for col in df.columns:
    #     print(col)

    # num linhas
    # print(len(df.index)) #cuidado ao usar outros tipos de formas pra achar o num de linhas, existem n jeitos de fazer uma coisa em python, um pior que o outro

    # valores unicos de cada coluna
    for col in df.columns:
        if col != 'id':
            print(df[col].drop_duplicates().sort_values())