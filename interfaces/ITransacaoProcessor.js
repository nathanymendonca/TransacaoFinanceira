
// Interface Segregation Principle (ISP)
class ITransacaoProcessor {
    processar(transacao) {
        throw new Error("Method 'processar' must be implemented");
    }
}

module.exports = ITransacaoProcessor;
