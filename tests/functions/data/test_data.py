import pytest
import numpy as np
import pandas
from mock import patch

from utils.functions.data.read import read_csv_with_header

class TestRead(object):
    def test_read_csv_with_header(self):
        with patch('pandas.read_csv') as mock_read_csv: # mock
            path = 'test'
            data = read_csv_with_header(path)
            mock_read_csv.assert_called_once()

if __name__ == '__main__':
    pytest.main()