
from models.conta_saldo import ContaSaldo
from interfaces.i_conta_repository import IContaRepository

class ContaRepository(IContaRepository):
    def __init__(self):
        self.tabela_saldos = [
            ContaSaldo(938485762, 180),
            ContaSaldo(347586970, 1200),
            ContaSaldo(2147483649, 0),
            ContaSaldo(675869708, 4900),
            ContaSaldo(238596054, 478),
            ContaSaldo(573659065, 787),
            ContaSaldo(210385733, 10),
            ContaSaldo(674038564, 400),
            ContaSaldo(563856300, 1200)
        ]

    def get_saldo(self, conta_id):
        return next((x for x in self.tabela_saldos if x.conta_id == conta_id), None)

    def atualizar_saldo(self, conta_saldo):
        try:
            for i, conta in enumerate(self.tabela_saldos):
                if conta.conta_id == conta_saldo.conta_id:
                    self.tabela_saldos[i] = conta_saldo
                    return True
            
            self.tabela_saldos.append(conta_saldo)
            return True
        except Exception as error:
            print(f"Erro ao atualizar saldo: {str(error)}")
            return False
