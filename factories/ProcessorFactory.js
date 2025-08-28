
const TransferenciaProcessor = require('../services/processors/TransferenciaProcessor');
const DepositoProcessor = require('../services/processors/DepositoProcessor');
const SaqueProcessor = require('../services/processors/SaqueProcessor');

class ProcessorFactory {
    static criarProcessor(tipo, contaRepository, logger) {
        switch (tipo.toUpperCase()) {
            case 'TRANSFERENCIA':
                return new TransferenciaProcessor(contaRepository, logger);
            case 'DEPOSITO':
                return new DepositoProcessor(contaRepository, logger);
            case 'SAQUE':
                return new SaqueProcessor(contaRepository, logger);
            default:
                throw new Error(`Tipo de processor '${tipo}' não suportado`);
        }
    }
}

module.exports = ProcessorFactory;
