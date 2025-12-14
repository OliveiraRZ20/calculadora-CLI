# Calculadora CLI

Uma calculadora simples para terminal (CLI) escrita em Python, com operações básicas de soma, subtração, multiplicação e divisão, validação de entradas do usuário e mensagens coloridas no console.

## Recursos
- **Operações**: soma, subtração, multiplicação e divisão.
- **Validação de entrada**: impede valores inválidos e divisão por zero.
- **UX no terminal**: limpeza de tela, pausa opcional e confirmação de saída.
- **Mensagens coloridas**: feedback informativo, de erro e confirmação.

## Pré-requisitos
- Python 3.10+ (testado em Windows; funciona também em Unix/macOS).

Verifique a versão instalada:
```bash
python --version
```
No Windows, o comando pode ser `py --version`.

## Como executar
1. Clone o repositório.
2. Execute diretamente o arquivo principal.

```bash
# Windows
python main.py

# Alternativa
python3 main.py
```

Ao iniciar, você verá o menu de operações:
```
| =============================================================== |
|             Bem-vindo à Calculadora no Terminal!                |
| =============================================================== |
| Operações disponíveis:                                          |
| 1. Soma                                                         |
| 2. Subtração                                                    |
| 3. Multiplicação                                                |
| 4. Divisão                                                      |
| 5. Sair                                                         |
| =============================================================== |
```

## Uso
- Escolha a operação digitando um número de 1 a 5.
- Informe os dois números (float) quando solicitado.
- O resultado é exibido em formato simples (sem notação científica desnecessária).
- Após cada operação, você pode confirmar a saída ou continuar usando a calculadora.

### Exemplos
- Soma: escolha `1`, digite `3` e `4` → Resultado: `7`
- Divisão por zero: escolha `4`, digite `10` e `0` → Alerta: "Divisão por zero não é permitida."

## Estrutura do projeto
```
LICENSE
main.py
README.md
src/
  __init__.py
  Calculadora.py
  utils/
    logger.py
    terminal.py
    user_input.py
```

- `main.py`: ponto de entrada da aplicação; mostra o menu e orquestra o fluxo.
- `src/Calculadora.py`: implementa `Calculadora` com os métodos `somar`, `subtrair`, `multiplicar`, `dividir` e `calcular`.
- `src/utils/user_input.py`: leitura segura de números (`ler_float`) e opções (`ler_opcao`).
- `src/utils/terminal.py`: utilidades de terminal (`cls`, `pause`, `finalizar_programa`, `confirmar_saida`).
- `src/utils/logger.py`: mensagens coloridas (`alertar`, `informar`, `confirmar`).

## Detalhes de implementação
- `Calculadora.calcular(a, b, operador)` encaminha para a operação correta.
- Proteção contra divisão por zero com alerta e retorno `None`.
- O resultado é impresso com formatação `:g` para evitar notação científica.
- O loop principal em `main.py` permite múltiplas operações até o usuário solicitar saída.

## Desenvolvimento
Não há dependências externas. Para rodar lint/format se desejar:
```bash
# Exemplos (opcionais, se instalados)
pip install ruff black
ruff .
black .
```

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE).

## Roadmap (idéias futuras)
- Histórico das operações no runtime.
- Suporte a mais operações (potência, raiz, porcentagem).
- Testes automatizados com `pytest`.
