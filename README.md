
# Sistema de Transações Financeiras - Python

Este é um sistema de transações financeiras implementado em Python que processa transferências, saques e depósitos entre contas, seguindo os princípios SOLID e padrões de design.

## Estrutura do Projeto

```
├── models/                        # Modelos de domínio
│   ├── conta_saldo.py             # Modelo para saldo da conta
│   └── transacao.py               # Modelo para transação

├── repositories/                  # Repositórios para acesso a dados
│   └── conta_repository.py        # Repositório de contas

├── services/                      # Serviços de negócio
│   ├── processors/                # Processadores específicos
│   │   ├── deposito_processor.py      # Processador de depósitos
│   │   ├── saque_processor.py         # Processador de saques
│   │   └── transferencia_processor.py # Processador de transferências
│   ├── logger.py                  # Serviço de logging
│   └── transacao_service.py       # Serviço principal de transações

├── interfaces/                    # Contratos e abstrações
│   ├── i_conta_repository.py      # Interface do repositório
│   └── i_transacao_processor.py   # Interface dos processadores

├── factories/                     # Factory para criação de processadores
│   └── processor_factory.py       # Factory de processadores

├── commands/                      # Padrão Command para transações
│   └── transacao_command.py       # Comando para transações

├── tests/                         # Testes unitários
│   ├── test_conta_repository.py   # Testes do repositório
│   └── test_transacao_service.py  # Testes do serviço

└── main.py                        # Ponto de entrada da aplicação
```

## Padrões e Princípios Implementados

### Princípios SOLID
- **SRP (Single Responsibility Principle)**: Cada classe tem uma única responsabilidade
- **OCP (Open/Closed Principle)**: Sistema aberto para extensão, fechado para modificação
- **LSP (Liskov Substitution Principle)**: Substituição de implementações sem quebrar funcionalidade
- **ISP (Interface Segregation Principle)**: Interfaces específicas e segregadas
- **DIP (Dependency Inversion Principle)**: Dependência de abstrações, não de concretizações

### Padrões de Design
- **Repository Pattern**: Abstração do acesso a dados
- **Strategy Pattern**: Diferentes estratégias de processamento
- **Factory Pattern**: Criação de objetos processadores
- **Command Pattern**: Encapsulamento de operações
- **Dependency Injection**: Injeção de dependências

## Como Executar

### Executar a aplicação:
```bash
python main.py
```

### Executar os testes:
```bash
python -m unittest discover tests -v
```

## Funcionalidades

- **Transferências**: Transferência de valores entre contas
- **Saques**: Retirada de valores de contas
- **Depósitos**: Adição de valores em contas
- **Validações**: Verificação de saldo e existência de contas
- **Logging**: Sistema de logs para auditoria

## Fluxo de uma Transação (Exemplo: Saque de R$100)

1. Entrada do Usuário
O usuário executa o programa (main.py) e solicita uma transação de saque.
O main envia essa requisição para o transacao_command.py.

2. Camada de Comando
O command interpreta a entrada e encaminha para o transacao_service.py, responsável por orquestrar a operação.

3. Serviço de Transação
No TransacaoService:
Cria um objeto Transacao (contendo conta, valor, tipo = "saque").
Chama a processor_factory.py para escolher qual processador usar.

4. Factory Pattern
A factory recebe o tipo da transação ("saque") e retorna o SaqueProcessor.
Assim, se fosse depósito, retornaria o DepositoProcessor; se transferência, o TransferenciaProcessor.

5. Processador da Transação
O SaqueProcessor executa a regra de negócio:
Verifica se a conta tem saldo suficiente.
Se sim, subtrai o valor (ex: -100).
Se não, lança exceção/erro.

➡️ Aqui o Strategy Pattern aparece: cada processador tem sua própria lógica, mas todos seguem a mesma interface (ITransacaoProcessor).

6. Atualização de Dados
O SaqueProcessor comunica-se com o conta_repository.py:
Atualiza o saldo da conta.
Também atualiza os models (ContaSaldo, Transacao) garantindo consistência.

7. Registro da Operação
O logger.py grava que um saque foi realizado, com detalhes (data, conta, valor).
Isso permite auditoria e rastreabilidade.

8. Resposta ao Usuário
O serviço retorna o resultado para o command, que devolve para o usuário no main.py:

✅ “Saque de R$100 realizado com sucesso.”

❌ “Saldo insuficiente.”

📌 Resumindo o caminho do saque:

main → command → service → factory → SaqueProcessor → repository/models/logger → resposta ao usuário




