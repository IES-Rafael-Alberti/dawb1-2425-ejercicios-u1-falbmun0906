import pytest

import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prueba1 import comparar_numero

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (1, 2, 2),
        (3, 5, 5),
        (-4, 4, 4)
    ]
)
def test_comparar_numero_params(input_x, input_y, expected):
    assert comparar_numero(input_x, input_y) == expected