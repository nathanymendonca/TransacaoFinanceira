
class Transacao {
    constructor(correlationId, dataHora, contaOrigem, contaDestino, valor) {
        this.correlationId = correlationId;
        this.dataHora = new Date(dataHora);
        this.contaOrigem = contaOrigem;
        this.contaDestino = contaDestino;
        this.valor = valor;
    }
}

module.exports = Transacao;
