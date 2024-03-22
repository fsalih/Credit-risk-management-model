import numpy as np
import pandas as pd

def split_and_save_pkl(df, part_count, filename='_part.pkl'):
    df.index = np.arange(df.shape[0])
    part_size = int(df.shape[0] / part_count)
    for i in range(part_count-1):
        df[i*part_size: (i+1)*part_size].to_pickle(f'{i}{filename}')
    df[(part_count-1)*part_size: ].to_pickle(f'{part_count-1}{filename}')
    print(f'{part_count} parts saved to [n]{filename}')
    
    