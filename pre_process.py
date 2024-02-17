import pandas as pd
import numpy as np
from tqdm import tqdm  # Import tqdm for the progress bar

class PreProcessRefString:

    def __init__(self) -> None:
        self.__path = 'dump'

    def set_path(self, path):
        self.__path = path

    def pre_process(self, reference_string):
        unique_pages, counts = np.unique(reference_string, return_counts=True)

        # Encontra a posição usando busca binária
        positions = np.searchsorted(unique_pages, reference_string, side='left')

        # Ajusta as posições para garantir que estejam dentro dos limites do array counts
        positions = np.clip(positions, 0, len(counts) - 1)

        # Cria um DataFrame usando pandas
        df = pd.DataFrame({'Page': reference_string, 'Next': counts[positions]})
        df['Next'] = np.where(df['Next'] == 1, np.Inf, df['Next'])  # Substitui -1 por np.Inf

        # Substitui os valores de acordo com a lógica do loop original

        # Use tqdm to create a progress bar
        for i in tqdm(range(len(df)), desc='Processing', unit='row'):
            if df['Next'].iloc[i] > 0:
                future = df.iloc[i+1:]
                mask = (future['Page'] == df['Page'].iloc[i])

                if mask.any():
                    df.at[i, 'Next'] = mask.idxmax() + i + 1
                else:
                    df.at[i, 'Next'] = np.Inf

        df.to_csv(self.__path + '.csv', index=False)

