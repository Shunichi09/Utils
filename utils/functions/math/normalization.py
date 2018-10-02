import math
import numpy as np
import copy 

def normalize_by_min_max(data):
    """ normalize the data in min and max of the all data 

    Parameters
    -----------
    data : array-like
        the data 

    Returns
    ----------
    normalized_data : numpy.ndarray
        the shape of array is same as the input data

    """

    data = np.array(data)
    data_shape = data.shape

    data = data.flatten()

    max_data = max(data)
    min_data = min(data)

    if max_data - min_data == 0:
        normalized_data = np.zeros_like(data_shape)
    else:
        normalized_data = (data - min_data) / (max_data - min_data)

    return normalized_data.reshape(data_shape)