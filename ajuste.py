import pandas as pd
import numpy as np
from sys import argv
from tqdm import tqdm 

if __name__ == '__main__':
    df = pd.read_csv(argv[1])

    index = np.array(df.index)
    df['Next'] -= index + 1

    df.to_csv(argv[1], index=False)
    pass