from pre_process import PreProcessRefString
from ref_string import GenRefString
import time

if __name__ == '__main__':
    log_filename = 'processing_times.log'

    with open(log_filename, 'w') as log_file:
        for i in range(1, 5):
            start_time = time.time()

            preProcess = PreProcessRefString()
            genRefString = GenRefString('logs/trace' + str(i))
            ref_string = genRefString.gen_ref_string()

            preProcess.set_path('logs/trace' + str(i))
            preProcess.pre_process(ref_string)

            end_time = time.time()
            elapsed_time = end_time - start_time

            log_file.write(f"Processing time for trace {i}: {elapsed_time} seconds\n")

    pass
