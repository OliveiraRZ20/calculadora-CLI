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
    def calcular(a: float, b: float, operador: int) -> tuple[bool, str, float | None]:
        if operador not in (1, 2, 3, 4):
            return (False, "Operador inválido.", None)
        elif operador == 4 and b == 0:
            return (False, "Divisão por zero não é permitida.", None)
        else:
            match operador:
                case 1:
                    resultado: float = Calculadora.somar(a, b)
                case 2:
                    resultado: float = Calculadora.subtrair(a, b)
                case 3:
                    resultado: float = Calculadora.multiplicar(a, b)
                case 4:
                    resultado: float = Calculadora.dividir(a, b)
            return (True, "Cálculo realizado com sucesso.", resultado)