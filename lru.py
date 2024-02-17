from collections import OrderedDict


class LRU:

    def __init__(self) -> None:
        pass
        
        

    @staticmethod
    def lru_page_replacement(reference_string, frames):
        page_faults = 0
        page_table = OrderedDict()

        for page in reference_string:
            # print(page_table)
            if page not in page_table:
                page_faults += 1
                if len(page_table) >= frames:
                    page_table.popitem(
                        last=False
                    )
                    # Remove a página menos recentemente usada
                page_table[page] = None  # Adiciona a página ao dicionário
            else:
                # Se a página já está na tabela, remova-a e readicione
                del page_table[page]
                page_table[page] = None

        return page_faults

