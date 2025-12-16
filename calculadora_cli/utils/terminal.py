# imports internos
from .logger import alertar, informar, confirmar

# imports externos
from os import system, name


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
