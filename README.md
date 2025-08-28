
# Sistema de Transações Financeiras - Node.js

Este é um sistema de transações financeiras implementado em Node.js que processa transferências entre contas.

## Estrutura do Projeto

```
├── models/
│   ├── ContaSaldo.js      # Modelo de conta e saldo
│   └── Transacao.js       # Modelo de transação
├── repositories/
│   └── ContaRepository.js # Repositório de contas
├── services/
│   └── TransacaoService.js # Serviço de transações
├── tests/
│   ├── ContaRepository.test.js
│   └── TransacaoService.test.js
├── index.js               # Arquivo principal
└── package.json
```

## Como executar

1. Instalar dependências:
```bash
npm install
```

2. Executar a aplicação:
```bash
npm start
```

## Como testar

```bash
npm test
```

## Funcionalidades

- Processamento de transações financeiras entre contas
- Validação de saldo suficiente
- Atualização automática de saldos
- Sistema de logging de transações
