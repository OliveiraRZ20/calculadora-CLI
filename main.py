from src.Calculadora import Calculadora
from src.Utils import Utils

def main():
    Utils.cls()
    print("| =============================================================== |")
    print("|             Bem-vindo à Calculadora no Terminal!                |")
    print("| =============================================================== |")
    print("| Operações disponíveis:                                          |")
    print("| 1. Soma                                                         |")
    print("| 2. Subtração                                                    |")
    print("| 3. Multiplicação                                                |")
    print("| 4. Divisão                                                      |")
    print("| =============================================================== |")
    operador: int = int(input("Digite o número da operação desejada (1-4): "))
    a: float = int(input("Digite o primeiro número: "))
    b: float = int(input("Digite o segundo número: "))
    resultado: float | None = Calculadora.calcular(a, b, operador)
    if resultado:
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    Utils.cls()
    while True:
        main()
        Utils.confirmar_saida()