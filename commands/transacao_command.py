
class TransacaoCommand:
    def __init__(self, transacao_service):
        self.transacao_service = transacao_service
    
    def executar_transferencia(self, transacao):
        return self.transacao_service.transferir(transacao)
    
    def executar_deposito(self, transacao):
        return self.transacao_service.depositar(transacao)
    
    def executar_saque(self, transacao):
        return self.transacao_service.sacar(transacao)
