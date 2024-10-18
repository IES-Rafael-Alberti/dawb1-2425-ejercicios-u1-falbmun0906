import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej05_def2 import precio_final

@pytest.mark.parametrize(
        "input_x, input_y, expected",
        [
            (200, 0.10, 220),
            (15, 0.03, 15.45),
            (44, 0.06, 46.64)
        ]
)
def test_precio_final(input_x, input_y, expected):
    assert precio_final(input_x, input_y) == expected