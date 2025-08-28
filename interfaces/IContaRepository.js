
// Interface Segregation Principle (ISP)
class IContaRepository {
    getSaldo(contaId) {
        throw new Error("Method 'getSaldo' must be implemented");
    }
    
    atualizarSaldo(contaSaldo) {
        throw new Error("Method 'atualizarSaldo' must be implemented");
    }
}

module.exports = IContaRepository;
