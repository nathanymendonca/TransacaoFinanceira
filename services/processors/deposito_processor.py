
from interfaces.i_transacao_processor import ITransacaoProcessor

class DepositoProcessor(ITransacaoProcessor):
    def __init__(self, conta_repository, logger):
        self.conta_repository = conta_repository
        self.logger = logger

    def processar(self, transacao):
        conta_saldo_destino = self.conta_repository.get_saldo(transacao.conta_destino)
        
        if not conta_saldo_destino:
            self.logger.log(f"Conta destino {transacao.conta_destino} não encontrada")
            return False

        conta_saldo_destino.saldo += transacao.valor
        self.conta_repository.atualizar_saldo(conta_saldo_destino)

        self.logger.log(f"Depósito numero {transacao.correlation_id} foi efetivado com sucesso! Novo saldo: {conta_saldo_destino.saldo}")
        return True
