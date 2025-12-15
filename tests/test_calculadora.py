import math
import pytest

from calculadora_cli.objects.calculadora import Calculadora


def test_somar_simples():
	assert Calculadora.somar(2, 3) == 5
	assert Calculadora.somar(-1, 1) == 0
	assert Calculadora.somar(0.1, 0.2) == pytest.approx(0.3, rel=1e-9, abs=1e-9)


def test_subtrair_simples():
	assert Calculadora.subtrair(5, 3) == 2
	assert Calculadora.subtrair(0, 3) == -3


def test_multiplicar_simples():
	assert Calculadora.multiplicar(4, 5) == 20
	assert Calculadora.multiplicar(-2, 3) == -6
	assert Calculadora.multiplicar(0, 99) == 0


def test_dividir_simples():
	assert Calculadora.dividir(10, 2) == 5
	assert Calculadora.dividir(-9, 3) == -3


def test_dividir_por_zero_retorna_none_via_calcular():
	# Operador 4 = divisão; quando b == 0 deve retornar None
	assert Calculadora.calcular(10, 0, 4) is None


def test_operador_invalido_retorna_none():
	assert Calculadora.calcular(1, 2, 999) is None


@pytest.mark.parametrize(
	"a,b,operador,esperado",
	[
		(2, 3, 1, 5),         # soma
		(5, 3, 2, 2),         # subtração
		(4, 5, 3, 20),        # multiplicação
		(10, 2, 4, 5),        # divisão
	],
)
def test_calcular_mapeia_operadores(a, b, operador, esperado):
	assert Calculadora.calcular(a, b, operador) == esperado

