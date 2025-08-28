
const ContaRepository = require('../repositories/ContaRepository');
const ContaSaldo = require('../models/ContaSaldo');

describe('ContaRepository', () => {
    let contaRepository;

    beforeEach(() => {
        contaRepository = new ContaRepository();
    });

    test('deve retornar saldo de conta existente', () => {
        // Act
        const resultado = contaRepository.getSaldo(938485762);

        // Assert
        expect(resultado).not.toBeNull();
        expect(resultado.saldo).toBe(180);
    });

    test('deve atualizar saldo com sucesso', () => {
        // Arrange
        const novaSaldo = new ContaSaldo(938485762, 200);

        // Act
        const resultado = contaRepository.atualizarSaldo(novaSaldo);

        // Assert
        expect(resultado).toBe(true);
        const contaAtualizada = contaRepository.getSaldo(938485762);
        expect(contaAtualizada.saldo).toBe(200);
    });
});
