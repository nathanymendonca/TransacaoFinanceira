
const Logger = require('./Logger');

// Open/Closed Principle (OCP) - Aberto para extensão, fechado para modificação
class TransacaoService {
    constructor(contaRepository) {
        this.contaRepository = contaRepository;
        this.logger = new Logger();
        this.processors = new Map();
    }

    // Dependency Inversion Principle (DIP) - Depende de abstração
    registrarProcessor(tipo, processor) {
        this.processors.set(tipo, processor);
    }

    // Single Responsibility Principle (SRP) - Responsabilidade de orquestrar o processamento
    transferir(transacao) {
        const processor = this.processors.get('TRANSFERENCIA');
        
        if (!processor) {
            this.logger.error('Processor para transferência não encontrado');
            return false;
        }

        return processor.processar(transacao);
    }
}

module.exports = TransacaoService;
