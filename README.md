
# Sistema de Transações Financeiras - Python

Este é um sistema de transações financeiras implementado em Python que processa transferências, saques e depósitos entre contas, seguindo os princípios SOLID e padrões de design.

## Estrutura do Projeto

```
├── models/                        # Modelos de domínio
│   ├── conta_saldo.py            # Modelo para saldo da conta
│   └── transacao.py              # Modelo para transação
├── repositories/                  # Repositórios para acesso a dados
│   └── conta_repository.py       # Repositório de contas
├── services/                      # Serviços de negócio
│   ├── processors/               # Processadores específicos
│   │   ├── deposito_processor.py # Processador de depósitos
│   │   ├── saque_processor.py    # Processador de saques
│   │   └── transferencia_processor.py # Processador de transferências
│   ├── logger.py                 # Serviço de logging
│   └── transacao_service.py      # Serviço principal de transações
├── interfaces/                    # Contratos e abstrações
│   ├── i_conta_repository.py     # Interface do repositório
│   └── i_transacao_processor.py  # Interface dos processadores
├── factories/                     # Factory para criação de processadores
│   └── processor_factory.py      # Factory de processadores
├── commands/                      # Padrão Command para transações
│   └── transacao_command.py      # Comando para transações
├── tests/                         # Testes unitários
│   ├── test_conta_repository.py  # Testes do repositório
│   └── test_transacao_service.py # Testes do serviço
└── main.py                       # Ponto de entrada da aplicação
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

## Dados de Teste

O sistema inclui contas pré-configuradas com saldos iniciais e um conjunto de transações de exemplo para demonstrar todas as funcionalidades.
