# Passo 1: Remover deslocamentos.
# Passo 2: Preencher 0s à esquerda.
# Passo 3: Remover/ignorar sequências de acesso a mesma página.
# Passo 4: Referenciar cada string e gerar a reference string
from sys import argv

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

with open("reference_string_" + argv[1], "w+") as clean_trace_file:
    for trace in clean_trace_list:
        clean_trace_file.write(trace + "\n")

unique_access_difference = len(clean_trace_list) / len(trace_list)

print(f"Original: {len(trace_list)} Novo: {len(clean_trace_list)}")
print(f"Diferença {100 * unique_access_difference:.3f}%")

import numpy as np

from collections import defaultdict


def optimal_page_replacement(reference_string, frames):
    page_faults = 0
    page_table = defaultdict(int)
    future_references = defaultdict(list)
    for i, page in enumerate(reference_string):
        if i % 1000 == 0:
            print(i)
        if page not in page_table:
            page_faults += 1
            if len(page_table) < frames:
                page_table[page] = i
            else:
                pages_to_remove = [
                    (p, future_references[p][-1])
                    for p in page_table
                    if p not in reference_string[i + 1 :]
                ]
                if pages_to_remove:
                    page_to_remove = max(pages_to_remove, key=lambda x: x[1])[0]
                    del page_table[page_to_remove]
                    page_table[page] = i
        future_references[page].append(i)

    return page_faults


from collections import OrderedDict


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
                )  # Remove a página menos recentemente usada
            page_table[page] = None  # Adiciona a página ao dicionário

    return page_faults


# lru_page_faults = []
# for i in range(2, 6):
#     page_faults = lru_page_replacement(clean_trace_list, 2**i)
#     lru_page_faults.append(page_faults)
#     print(f"Número de falhas LRU: {page_faults}")

# opt_page_faults = []
# for i in range(2, 6):
#     page_faults = optimal_page_replacement(clean_trace_list, 2**i)
#     opt_page_faults.append(page_faults)
#     print(f"Número de falhas OPT: {page_faults}")


# import matplotlib.pyplot as plt
# plt.plot([4, 8, 16, 32], opt_page_faults)

# plt.xlabel("Qtd. de frames")
# plt.ylabel("Falhas")
# plt.title("Falhas de página")
# plt.show()


# Function to check whether a page exists in a frame or not
def search(key, fr):
    for i in range(len(fr)):
        if fr[i] == key:
            return True
    return False


# Function to find the frame that will not be used
# recently in future after given index in pg[0..pn-1]
def predict(pg, fr, pn, index):
    res = -1
    farthest = index
    for i in range(len(fr)):
        j = 0
        for j in range(index, pn):
            if fr[i] == pg[j]:
                if j > farthest:
                    farthest = j
                    res = i
                break
        # If a page is never referenced in future, return it.
        if j == pn:
            return i
    # If all of the frames were not in future, return any of them, we return 0. Otherwise we return res.
    return 0 if (res == -1) else res


def optimalPage(pg, pn, fn):

    # Create an array for given number of frames and initialize it as empty.
    fr = []

    # Traverse through page reference array and check for miss and hit.
    hit = 0
    for i in range(pn):
        if i % 1000 == 0:
            print(i)

        # Page found in a frame : HIT
        if search(pg[i], fr):
            hit += 1
            continue

        # Page not found in a frame : MISS
        # If there is space available in frames.
        if len(fr) < fn:
            fr.append(pg[i])

        # Find the page to be replaced.
        else:
            j = predict(pg, fr, pn, i + 1)
            fr[j] = pg[i]
    print("No. of hits =", hit)
    print("No. of misses =", pn-hit)


# Driver Code
# pg = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
pg = clean_trace_list
pn = len(pg)
fn = 4
optimalPage(pg, pn, fn)

# This code is contributed by Marlon.

# {1, 2, 3, 4}  1, 5, 3, 8, 7, 