# Passo 1: Remover deslocamentos.
# Passo 2: Preencher 0s à esquerda.
# Passo 3: Remover/ignorar sequências de acesso a mesma página.
# Passo 4: Referenciar cada string e gerar a reference string
import numpy as np # Vetores otimizados e funções vetoriais úteis
import matplotlib.pyplot as plt # Gráficos/Visualização
from os import remove
from sys import argv # Argv para fácil teste
from collections import OrderedDict

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

def optimal_page_replacement(reference_string, frames):
    page_faults = 0
    page_table = OrderedDict()



    return page_faults


# LRU

def lru_page_replacement(reference_string, frames):
    page_faults = 0
    page_table = []

    for page in reference_string:
        # print(page_table)
        if page not in page_table:
            page_faults += 1
            if len(page_table) >= frames:
                page_table.pop() # Remove a página menos recentemente usada
            page_table.insert(0, page)

    return page_faults


lru_page_faults = []
for i in range(2, 6):
    page_faults = lru_page_replacement(clean_trace_list, 2**i)
    lru_page_faults.append(page_faults)
    print(f"Número de falhas LRU: {page_faults}")

# opt_page_faults = []
# for i in range(2, 6):
#     page_faults = optimal_page_replacement(clean_trace_list, 2**i)
#     opt_page_faults.append(page_faults)
#     print(f"Número de falhas OPT: {page_faults}")

plt.plot([4, 8, 16, 32], lru_page_faults)

plt.xlabel("Qtd. de frames")
plt.ylabel("Falhas")
plt.title("Falhas de página")
plt.show()

if ("-r" in argv):
    remove("reference_string_" + argv[1])
