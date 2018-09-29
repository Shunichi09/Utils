# 標準ライブラリ
import pandas as pd
import numpy as np

def read_csv_with_header(path):
    '''
    Read csv data and translate to numpy.ndarray with headers
    You can use this function when you want to read csv with header as data

    Parameters
    -------
    path : strings
        csv file's path
    
    Returns
    -------
    data : numpy.ndarray
    '''

    data = pd.read_csv(path, header=None, engine='python')
    data = data.values # testまだしてない

    return data