from os import system, name
from src.utils.logger import alertar, informar, confirmar

def cls():
    """Limpa a tela do terminal."""
    system('cls' if name == 'nt' else 'clear')

def pause():
    """Pausa a execução até que o usuário pressione Enter."""
    input("Pressione Enter para continuar...")

def finalizar_programa():
    """Finaliza o programa com uma mensagem de confirmação."""
    confirmar("Programa finalizado com sucesso!")
    exit(0)

def confirmar_saida():
    """Confirma se o usuário deseja sair do programa."""
    resposta: str = input("Deseja finalizar o programa? (s/n): ").strip().lower()
    if resposta == 's':
        finalizar_programa()