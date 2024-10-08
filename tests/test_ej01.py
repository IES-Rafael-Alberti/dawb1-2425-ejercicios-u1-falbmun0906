import pytest

import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej01_def import saludo

def test_saludo():
    assert saludo("Fran") == "Hola, Fran."
    assert saludo("Pepe") == "Hola, Pepe."
    assert saludo("Sara") == "Hola, Sara."
    assert saludo("") == "Hola, ."

if __name__ == "__main__":
    pytest.main()