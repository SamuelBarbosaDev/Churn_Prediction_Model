import pandas as pd
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder
from DataUnderstanding import DataUnderstanding


class DataPreparetion(DataUnderstanding):
    def removendo_nulos(self, dataframe: pd.DataFrame, colunas: list) -> pd.DataFrame:
        return dataframe.dropna(subset=colunas)

    def removendo_colunas(self, dataframe: pd.DataFrame, colunas=[]) -> pd.DataFrame:
        return dataframe.drop(colunas, axis=1)

    def renomeando_colunas(self, dataframe: pd.DataFrame, velho_nome_e_novo_nome: dict) -> pd.DataFrame:
        return dataframe.rename(columns=velho_nome_e_novo_nome)

    def substituindo_valores(self, dataframe: pd.DataFrame, colunas: list, valores: dict) -> pd.DataFrame:
        return dataframe[colunas].replace(valores)

    def convertendo_colunas(self, dataframe: pd.DataFrame, colunas, tipo: str) -> pd.DataFrame:
        return dataframe[colunas].astype(tipo)

    def dummy(self, dataframe: pd.DataFrame, colunas: list) -> (pd.DataFrame, list):
        dataframe = pd.get_dummies(dataframe[colunas])
        colunas = dataframe.columns
        return dataframe, colunas

    def label_endcode(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        training = LabelEncoder().fit(dataframe)
        dataframe = training.transform(dataframe)
        return dataframe

    def normalizando_os_dados(self, dataframe: pd.DataFrame) -> list:
        return scale(dataframe)


if __name__ == '__main__':
    data_preparetion = DataPreparetion()
