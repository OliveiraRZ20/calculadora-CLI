from src.Utils import Utils

class Calculadora():
    
    @staticmethod
    def somar(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def subtrair(a: float, b: float) -> float:
        return a - b
    
    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def dividir(a: float, b: float) -> float:
        return a / b
    
    @staticmethod
    def calcular(a: float, b: float, operador: int) -> float | None:
        if operador == 1:
            return Calculadora.somar(a, b)
        if operador == 2:
            return Calculadora.subtrair(a, b)
        if operador == 3:
            return Calculadora.multiplicar(a, b)
        if operador == 4:
            if b == 0:
                Utils.alertar("Divisão por zero não é permitida.")
                return None
            return Calculadora.dividir(a, b)
        else:
            Utils.alertar("Operador inválido.")
            return None
