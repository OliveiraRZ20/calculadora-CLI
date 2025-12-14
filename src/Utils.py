from os import system, name

class Utils():
    
    @staticmethod
    def cls():
        """Limpa a tela do terminal."""
        system('cls' if name == 'nt' else 'clear')
    
    @staticmethod
    def pause():
        """Pausa a execução até que o usuário pressione Enter."""
        input("Pressione Enter para continuar...")
    
    @staticmethod
    def confirmar_saida():
        """Confirma se o usuário deseja sair do programa."""
        resposta: str = input("Deseja finalizar o programa? (s/n): ").strip().lower()
        if resposta == 's':
            Utils.confirmar("Programa finalizado com sucesso!")
            exit(0)
    
    @staticmethod
    def alertar(msg: str) -> None:
        """Exibe uma mensagem de alerta no terminal na cor VERMELHA."""
        print(f"\033[31m[ERRO] {msg}\033[0m")

    @staticmethod
    def informar(msg: str) -> None:
        """Exibe uma mensagem informativa no terminal na cor AMARELA."""
        print(f"\033[33m[INFO] {msg}\033[0m")

    @staticmethod
    def confirmar(msg: str) -> None:
        """Exibe uma mensagem de confirmação no terminal na cor VERDE."""
        print(f"\033[32m[SUCESSO] {msg}\033[0m")