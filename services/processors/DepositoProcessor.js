
const ITransacaoProcessor = require('../../interfaces/ITransacaoProcessor');

class DepositoProcessor extends ITransacaoProcessor {
    constructor(contaRepository, logger) {
        super();
        this.contaRepository = contaRepository;
        this.logger = logger;
    }

    processar(transacao) {
        const contaDestino = this.contaRepository.getSaldo(transacao.contaDestino);
        
        if (!contaDestino) {
            this.logger.log(`Conta ${transacao.contaDestino} não encontrada para depósito`);
            return false;
        }

        contaDestino.saldo += transacao.valor;
        this.contaRepository.atualizarSaldo(contaDestino);

        this.logger.log(`Depósito ${transacao.correlationId} processado. Novo saldo: ${contaDestino.saldo}`);
        return true;
    }
}

module.exports = DepositoProcessor;
