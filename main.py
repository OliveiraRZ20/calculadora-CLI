from src.Calculadora import Calculadora
from src.utils.logger import alertar, informar, confirmar
from src.utils.terminal import cls, pause, finalizar_programa, confirmar_saida
from src.utils.user_input import ler_float, ler_opcao

def main():
    cls()
    print("| =============================================================== |")
    print("|             Bem-vindo à Calculadora no Terminal!                |")
    print("| =============================================================== |")
    print("| Operações disponíveis:                                          |")
    print("| 1. Soma                                                         |")
    print("| 2. Subtração                                                    |")
    print("| 3. Multiplicação                                                |")
    print("| 4. Divisão                                                      |")
    print("| 5. Sair                                                         |")
    print("| =============================================================== |")
    operador: int = ler_opcao("Digite o número da operação desejada (1-5): ", [1, 2, 3, 4, 5])
    if operador == 5:
        finalizar_programa()
    a: float = ler_float("Digite o primeiro número: ")
    b: float = ler_float("Digite o segundo número: ")
    resultado: float | None = Calculadora.calcular(a, b, operador)
    if resultado:
        print(f"Resultado: {resultado:g}") # :g para evitar notação científica desnecessária

if __name__ == "__main__":
    cls()
    while True:
        main()
        confirmar_saida()