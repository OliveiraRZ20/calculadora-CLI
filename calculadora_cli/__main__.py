import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# imports internos
from calculadora_cli.objects import Calculadora
from calculadora_cli.utils import terminal, user_input

# imports externos


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
    print("| =============================================================== |")
    operador: int = user_input.ler_opcao(prompt="Digite o número da operação desejada (1-4): ", opcoes_disponiveis=[1, 2, 3, 4])
    a: float = user_input.ler_float(prompt="Digite o primeiro número: ")
    b: float = user_input.ler_float(prompt="Digite o segundo número: ")
    
    resultado, mensagem, valor = Calculadora.calcular(a, b, operador)
    match resultado:
        case True:
            print(f"Resultado: {valor:g}") # :g para evitar notação científica desnecessária
        case False:
            terminal.alertar(mensagem)

if __name__ == "__main__":
    try:
        while True:
            main()
            terminal.pause()
    except KeyboardInterrupt:
        print("")
        terminal.finalizar_programa()