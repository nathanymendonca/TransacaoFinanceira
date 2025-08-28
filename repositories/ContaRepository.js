
const ContaSaldo = require('../models/ContaSaldo');

class ContaRepository {
    constructor() {
        this.tabelaSaldos = [
            new ContaSaldo(938485762, 180),
            new ContaSaldo(347586970, 1200),
            new ContaSaldo(2147483649, 0),
            new ContaSaldo(675869708, 4900),
            new ContaSaldo(238596054, 478),
            new ContaSaldo(573659065, 787),
            new ContaSaldo(210385733, 10),
            new ContaSaldo(674038564, 400),
            new ContaSaldo(563856300, 1200)
        ];
    }

    getSaldo(contaId) {
        return this.tabelaSaldos.find(x => x.contaId === contaId);
    }

    atualizarSaldo(contaSaldo) {
        try {
            const index = this.tabelaSaldos.findIndex(x => x.contaId === contaSaldo.contaId);
            if (index !== -1) {
                this.tabelaSaldos[index] = contaSaldo;
            } else {
                this.tabelaSaldos.push(contaSaldo);
            }
            return true;
        } catch (error) {
            console.log(`Erro ao atualizar saldo: ${error.message}`);
            return false;
        }
    }
}

module.exports = ContaRepository;
