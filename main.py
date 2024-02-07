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
    while (len(trace_list[i]) != 5):
        trace_list[i] = "0" + trace_list[i]

# Passo 3
    
clean_trace_list.append(trace_list[0])
previous_trace = trace_list[0]

for i in range(1, len(trace_list)):
    if (trace_list[i] != previous_trace):
        clean_trace_list.append(trace_list[i])
    previous_trace = trace_list[i]

with open(argv[1] + "_clean", "w+") as clean_trace_file:
    for trace in clean_trace_list:
        clean_trace_file.write(trace + '\n')

unique_access_difference =  len(trace_list) - len(clean_trace_list)

print(f"Original: {len(trace_list)} Novo: {len(clean_trace_list)}")
print(f"Diferença {unique_access_difference}")
