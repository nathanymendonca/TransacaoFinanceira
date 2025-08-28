
const ITransacaoProcessor = require('../../interfaces/ITransacaoProcessor');

class SaqueProcessor extends ITransacaoProcessor {
    constructor(contaRepository, logger) {
        super();
        this.contaRepository = contaRepository;
        this.logger = logger;
    }

    processar(transacao) {
        const contaOrigem = this.contaRepository.getSaldo(transacao.contaOrigem);
        
        if (!contaOrigem) {
            this.logger.log(`Conta ${transacao.contaOrigem} não encontrada para saque`);
            return false;
        }

        if (contaOrigem.saldo < transacao.valor) {
            this.logger.log(`Saque ${transacao.correlationId} cancelado por saldo insuficiente`);
            return false;
        }

        contaOrigem.saldo -= transacao.valor;
        this.contaRepository.atualizarSaldo(contaOrigem);

        this.logger.log(`Saque ${transacao.correlationId} processado. Novo saldo: ${contaOrigem.saldo}`);
        return true;
    }
}

module.exports = SaqueProcessor;
