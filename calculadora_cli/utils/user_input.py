from utils.logger import alertar, informar, confirmar

def ler_float(prompt: str) -> float:
    """Lê um número float do usuário, exibindo o prompt fornecido."""
    while True:
        try:
            valor: float = float(input(prompt))
            return valor
        except ValueError:
            alertar("Entrada inválida. Por favor, digite um número válido.")

def ler_opcao(prompt: str, opcoes_disponiveis: list) -> int:
    """Lê uma opção do usuário dentre as opções fornecidas."""
    while True:
        try:
            valor: int = int(input(prompt))
            if valor in opcoes_disponiveis:
                return valor
            else:
                alertar(f"Opção inválida. Por favor, escolha entre {opcoes_disponiveis}.")
        except ValueError:
            alertar("Entrada inválida. Por favor, digite um número válido.")