from objects import Calculadora
import utils.terminal as terminal
import utils.user_input as user_input


def main():
    terminal.cls()
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
    operador: int = user_input.ler_opcao(prompt="Digite o número da operação desejada (1-5): ", opcoes_disponiveis=[1, 2, 3, 4, 5])
    if operador == 5:
        terminal.finalizar_programa()
    a: float = user_input.ler_float(prompt="Digite o primeiro número: ")
    b: float = user_input.ler_float(prompt="Digite o segundo número: ")
    resultado: float | None = Calculadora.calcular(a, b, operador)
    if resultado:
        print(f"Resultado: {resultado:g}") # :g para evitar notação científica desnecessária

if __name__ == "__main__":
    try:
        terminal.cls()
        while True:
            main()
            terminal.confirmar_saida()
    except KeyboardInterrupt:
        print("")
        terminal.finalizar_programa()