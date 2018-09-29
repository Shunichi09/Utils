import pytest
import numpy as np
import pandas
from mock import patch

from utils.func_data import read_csv_with_header

def test_read_csv_with_header():
    with patch('pandas.read_csv') as mock_read_csv: # mock
        path = 'test'
        data = read_csv_with_header(path)
        mock_read_csv.assert_called_once()