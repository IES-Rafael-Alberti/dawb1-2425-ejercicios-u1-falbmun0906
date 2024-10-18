import pytest

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej02_def import salario

@pytest.mark.parametrize(
        "input_x, input_y, expected",
        [
            (2, 2, 4),
            (3, 10, 30),
            (5, 6, 30)
        ]
)
def test_salario_params(input_x, input_y, expected):
    assert salario(input_x, input_y) == expected