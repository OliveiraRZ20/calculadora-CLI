import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# imports internos
from calculadora_cli.objects import Calculadora

# imports externos
import pytest

class TestCalculadora:
    def test_somar(self):
        assert Calculadora.somar(2, 3) == 5
        assert Calculadora.somar(-1, 1) == 0

    def test_subtrair(self):
        assert Calculadora.subtrair(5, 3) == 2
        assert Calculadora.subtrair(0, 0) == 0

    def test_multiplicar(self):
        assert Calculadora.multiplicar(4, 2) == 8
        assert Calculadora.multiplicar(-1, -1) == 1

    def test_dividir(self):
        assert Calculadora.dividir(6, 2) == 3
        assert Calculadora.dividir(-4, 2) == -2

    def test_calcular_somar(self):
        resultado = Calculadora.calcular(2, 3, 1)
        assert resultado == (True, "Cálculo realizado com sucesso.", 5)

    def test_calcular_subtrair(self):
        resultado = Calculadora.calcular(5, 3, 2)
        assert resultado == (True, "Cálculo realizado com sucesso.", 2)

    def test_calcular_multiplicar(self):
        resultado = Calculadora.calcular(4, 2, 3)
        assert resultado == (True, "Cálculo realizado com sucesso.", 8)

    def test_calcular_dividir(self):
        resultado = Calculadora.calcular(6, 2, 4)
        assert resultado == (True, "Cálculo realizado com sucesso.", 3)

    def test_calcular_divisao_por_zero(self):
        resultado = Calculadora.calcular(6, 0, 4)
        assert resultado == (False, "Divisão por zero não é permitida.", None)

    def test_calcular_operador_invalido(self):
        resultado = Calculadora.calcular(6, 2, 5)
        assert resultado == (False, "Operador inválido.", None)