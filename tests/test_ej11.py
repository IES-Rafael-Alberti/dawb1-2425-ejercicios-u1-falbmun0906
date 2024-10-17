import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej11_def import suma

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (5, "15"),  
        (10, "55"),
        (0, "0"),   
        (1, "1")    
    ]
)
def test_suma(input_num, expected):
    assert suma(input_num) == expected