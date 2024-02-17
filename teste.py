from lru import LRU
from opt import OPT
from ref_string import GenRefString
import time

if __name__ == '__main__':
        
    log_filename = 'page_faults.log'

    with open(log_filename, 'a') as log_file:
        for i in range(1, 5):
            for frames in range(2, 6):

                genRefString = GenRefString('logs/trace' + str(i))
                ref_string = genRefString.gen_ref_string()
                redu = genRefString.get__reduction()
                ref_size, original_size = genRefString.get__sizes()
                
                start_time = time.time()

                page_faults = LRU.lru_page_replacement(ref_string, 2**frames)

                end_time = time.time()
                
                elapsed_time = end_time - start_time

                log_file.write(f"trace{i},{ref_size},{original_size},{100*redu:.4f},{2**frames},LRU,{page_faults},{elapsed_time}\n")

                
                start_time = time.time()

                page_faults = OPT.optimal_page_replacement(f'logs/trace{i}.csv', 2**frames)

                end_time = time.time()

                elapsed_time = end_time - start_time
            
                log_file.write(f"trace{i},{ref_size},{original_size},{100*redu:.4f},{2**frames},OPT,{page_faults},{elapsed_time}\n")



# for i in range(2, 6):
#     page_faults = lru_page_replacement(clean_trace_list, 2**i)
#     lru_page_faults.append(page_faults)
#     print(f"Número de falhas LRU: {page_faults}")
                
# trace1 , ref_size, original_size, redu, frames, alg  , page_faults , tempo