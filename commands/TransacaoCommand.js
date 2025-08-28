
class TransacaoCommand {
    constructor(transacao, processor) {
        this.transacao = transacao;
        this.processor = processor;
        this.executado = false;
    }

    execute() {
        if (!this.executado) {
            this.resultado = this.processor.processar(this.transacao);
            this.executado = true;
            return this.resultado;
        }
        return false;
    }

    undo() {
        // Implementar lógica de reversão se necessário
        throw new Error("Undo não implementado para este comando");
    }

    isExecuted() {
        return this.executado;
    }
}

module.exports = TransacaoCommand;
