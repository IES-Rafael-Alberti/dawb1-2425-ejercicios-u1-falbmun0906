import pytest

import sys
import os

# Agregar el directorio raíz del proyecto al sys.path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ej04_def import conversion_a_celsius

def test_conversion_a_celsius(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "100")
    
    resultado = conversion_a_celsius()

    assert resultado == "La temperatura en grados Celsius es: 37.78ºC (100.00ºF)"

def test_conversion_a_celsius_float(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "98.6")
    
    resultado = conversion_a_celsius()

    assert resultado == "La temperatura en grados Celsius es: 37.00ºC (98.60ºF)"