
const TransacaoService = require('../services/TransacaoService');
const ContaSaldo = require('../models/ContaSaldo');
const Transacao = require('../models/Transacao');

// Mock do ContaRepository
class MockContaRepository {
    constructor() {
        this.contas = new Map();
    }

    getSaldo(contaId) {
        return this.contas.get(contaId);
    }

    atualizarSaldo(contaSaldo) {
        this.contas.set(contaSaldo.contaId, contaSaldo);
        return true;
    }

    setup(contaId, contaSaldo) {
        this.contas.set(contaId, contaSaldo);
    }
}

describe('TransacaoService', () => {
    let transacaoService;
    let mockContaRepository;

    beforeEach(() => {
        mockContaRepository = new MockContaRepository();
        transacaoService = new TransacaoService(mockContaRepository);
    });

    test('deve realizar transferência válida', () => {
        // Arrange
        const contaOrigem = new ContaSaldo(938485762, 150);
        const contaDestino = new ContaSaldo(2147483649, 0);

        mockContaRepository.setup(938485762, contaOrigem);
        mockContaRepository.setup(2147483649, contaDestino);

        const transacao = new Transacao(1, "09/09/2023 14:15:00", 938485762, 2147483649, 100);

        // Act
        transacaoService.transferir(transacao);

        // Assert
        expect(contaOrigem.saldo).toBe(50);
        expect(contaDestino.saldo).toBe(100);
    });

    test('deve cancelar transferência por falta de saldo', () => {
        // Arrange
        const contaOrigem = new ContaSaldo(938485762, 50);
        const contaDestino = new ContaSaldo(2147483649, 0);

        mockContaRepository.setup(938485762, contaOrigem);
        mockContaRepository.setup(2147483649, contaDestino);

        const transacao = new Transacao(1, "09/09/2023 14:15:00", 938485762, 2147483649, 100);

        // Act
        transacaoService.transferir(transacao);

        // Assert
        expect(contaOrigem.saldo).toBe(50); // Saldo não deveria mudar
        expect(contaDestino.saldo).toBe(0); // Saldo não deveria mudar
    });
});
