# %load q08_get_total_extras/build.py
# Default Imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = 'data/ipl_matches_small.csv'

def get_total_extras():
    ipl_match_array=read_ipl_data_csv(path,'|S50')
    total_extras=np.sum(ipl_match_array[:,17].astype(np.int))

    return total_extras

get_total_extras()

# Enter Code Here
