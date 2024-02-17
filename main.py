# Passo 1: Remover deslocamentos.
# Passo 2: Preencher 0s à esquerda.
# Passo 3: Remover/ignorar sequências de acesso a mesma página.
# Passo 4: Referenciar cada string e gerar a reference string
import numpy as np  # Vetores otimizados e funções vetoriais úteis
import matplotlib.pyplot as plt  # Gráficos/Visualização
import time
from os import remove, path
from sys import argv  # Argv para fácil teste
import pickle

trace_list = []
clean_trace_list = []

with open(argv[1]) as trace_file:
    trace_list = trace_file.readlines()
    for i in range(len(trace_list)):
        trace_list[i] = trace_list[i].strip()

# Passo 1

for i in range(len(trace_list)):
    trace_list[i] = trace_list[i][:-3]

# Passo 2

for i in range(len(trace_list)):
    while len(trace_list[i]) != 5:
        trace_list[i] = "0" + trace_list[i]

# Passo 3

clean_trace_list.append(trace_list[0])
previous_trace = trace_list[0]

for i in range(1, len(trace_list)):
    if trace_list[i] != previous_trace:
        clean_trace_list.append(trace_list[i])
    previous_trace = trace_list[i]

# Salvar Reference String

with open("reference_string_" + argv[1], "w+") as clean_trace_file:
    for trace in clean_trace_list:
        clean_trace_file.write(trace + "\n")

unique_access_difference = len(clean_trace_list) / len(trace_list)

print(f"Original: {len(trace_list)} Novo: {len(clean_trace_list)}")
print(f"Diferença {100 * unique_access_difference:.3f}%")

# Simular Algoritmos


# OPT

def opt_find_positional_table(reference_string: list[str]) -> dict[str, list[int]]:
    if (path.exists("positional_table_" + argv[1] + ".pickle")):
        positional_table = pickle.load(open("positional_table_" + argv[1] + ".pickle", "rb"))
        return positional_table
    positional_table = {}
    i = 0
    original_length = len(reference_string)
    while (len(reference_string) > 0):
        print("Table Progress:", i)
        if reference_string[0] in positional_table:
            positional_table[reference_string[0]].append(i)
        else:
            positional_table[reference_string[0]] = [i]
        reference_string.pop(0)
        i += 1
    for key in positional_table.keys():
        positional_table[key].append(original_length)
    with open("positional_table_" + argv[1], "w+") as positional_table_file:
        for key, value in positional_table.items():
            positional_table_file.write(f"{key} {value}\n")
    pickle_file = open("positional_table_" + argv[1] + ".pickle", "wb")
    pickle.dump(positional_table, pickle_file)
    pickle_file.close()
    return positional_table



def optimal_page_replacement(reference_string: list[str], frames: int):
    page_faults = 0
    positions_table = opt_find_positional_table(reference_string)
    page_table = []
    page_amount_count = 0
    for i in range(len(reference_string)):
        if i % 1000 == 0:
            print(i)
        if not reference_string[i] in page_table:
            positions_table[reference_string[i]].pop(0)
            page_faults += 1
            if page_amount_count >= frames:
                max_index = 0
                for i in range(1, len(page_table)):
                    if positions_table[page_table[i]][0] > max_index:
                        max_index = i                        
                page_table[max_index] = reference_string[i]
            else:
                page_table.append(reference_string[i])
                page_amount_count += 1
    return page_faults


# LRU


def lru_page_replacement(reference_string: list[str], frames: int):
    page_faults = 0
    page_table = []

    for page in reference_string:
        # print(page_table)
        if page not in page_table:
            page_faults += 1
            if len(page_table) >= frames:
                page_table.pop()  # Remove a página menos recentemente usada
            page_table.insert(0, page)

    return page_faults


lru_page_faults = []
for i in range(2, 6):
    page_faults = lru_page_replacement(clean_trace_list, 2**i)
    lru_page_faults.append(page_faults)
    print(f"Número de falhas LRU: {page_faults}")

opt_page_faults = []
for i in range(2, 6):
    page_faults = optimal_page_replacement(clean_trace_list, 2**i)
    opt_page_faults.append(page_faults)
    print(f"Número de falhas OPT: {page_faults}")

plt.plot([4, 8, 16, 32], lru_page_faults)

plt.xlabel("Qtd. de frames")
plt.ylabel("Falhas")
plt.title("Falhas de página")
plt.show()

plt.plot([4, 8, 16, 32], opt_page_faults)

plt.xlabel("Qtd. de frames")
plt.ylabel("Falhas")
plt.title("Falhas de página")
plt.show()

if "-r" in argv:
    remove("reference_string_" + argv[1])
