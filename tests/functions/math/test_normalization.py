import pytest 
import random
import math
import numpy as np
from utils.functions.math.normalization import normalize_by_min_max

class Testnormalization(object):
    def test_normalize_by_min_max_scalar(self):
        data = np.random.rand(100) * 3.0 + 2.1
        normalized_data = normalize_by_min_max(data)

        assert data.shape == normalized_data.shape
        assert np.argmax(data) == np.argmax(normalized_data)
        assert np.argmin(data) == np.argmin(normalized_data)

        for i in range(len(data)):
            if normalized_data[i] > 1.0 or normalized_data[i] < 0.0:
                assert False        
    
    def test_normalize_by_min_max_matrix(self):
        data = np.random.rand(3, 100) * 3.0 - 2.1
        normalized_data = normalize_by_min_max(data)

        assert data.shape == normalized_data.shape
        assert np.argmax(data) == np.argmax(normalized_data)
        assert np.argmin(data) == np.argmin(normalized_data)

        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                if normalized_data[i, j] > 1.0 or normalized_data[i, j] < 0.0:
                    assert False

if __name__ == '__main__':
    pytest.main()