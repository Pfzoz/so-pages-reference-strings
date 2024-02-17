import pandas as pd
from tqdm import tqdm

class OPT:
    def __init__(self) -> None:
        pass

    @staticmethod
    def optimal_page_replacement(path, frames):
        page_faults = 0
        page_table = {}

        df = pd.read_csv(path)

        # Use tqdm to create a progress bar
        for _, row in tqdm(df.iterrows(), total=len(df), desc="Processing rows"):
            if row['Page'] not in page_table:
                page_faults += 1
                # Se a tabela ainda tem frames livres
                if len(page_table) < frames:
                    page_table[row['Page']] = row['Next']
                else:
                    # Caso não retorna o max
                    max_key = max(page_table, key=lambda k: page_table[k])
                    # Deleta pagina max
                    del page_table[max_key]
                    # Adiciona a linha atual ao dicionário
                    page_table[row['Page']] = row['Next']

            else:
                # Caso a pagina ja esteja, ele atualiza a o Next da pagina
                page_table[row['Page']] = row['Next']

        # Retorna o total de falhas de página
        return page_faults

if __name__ == '__main__':
    print(OPT.optimal_page_replacement('logs/trace1.csv', 4))
