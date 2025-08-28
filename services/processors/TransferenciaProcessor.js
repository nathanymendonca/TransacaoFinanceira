
const ITransacaoProcessor = require('../../interfaces/ITransacaoProcessor');

// Single Responsibility Principle (SRP) - Responsabilidade específica para transferências
class TransferenciaProcessor extends ITransacaoProcessor {
    constructor(contaRepository, logger) {
        super();
        this.contaRepository = contaRepository;
        this.logger = logger;
    }

    processar(transacao) {
        const contaSaldoOrigem = this.contaRepository.getSaldo(transacao.contaOrigem);
        
        if (!contaSaldoOrigem) {
            this.logger.log(`Conta origem ${transacao.contaOrigem} não encontrada`);
            return false;
        }
        
        if (contaSaldoOrigem.saldo < transacao.valor) {
            this.logger.log(`Transacao numero ${transacao.correlationId} foi cancelada por falta de saldo`);
            return false;
        }

        const contaSaldoDestino = this.contaRepository.getSaldo(transacao.contaDestino);
        
        if (!contaSaldoDestino) {
            this.logger.log(`Conta destino ${transacao.contaDestino} não encontrada`);
            return false;
        }

        contaSaldoOrigem.saldo -= transacao.valor;
        contaSaldoDestino.saldo += transacao.valor;

        this.contaRepository.atualizarSaldo(contaSaldoOrigem);
        this.contaRepository.atualizarSaldo(contaSaldoDestino);

        this.logger.log(`Transacao numero ${transacao.correlationId} foi efetivada com sucesso! Novos saldos: Conta Origem: ${contaSaldoOrigem.saldo} | Conta Destino: ${contaSaldoDestino.saldo}`);
        return true;
    }
}

module.exports = TransferenciaProcessor;
