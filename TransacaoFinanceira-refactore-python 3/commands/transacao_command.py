
class TransacaoCommand:
    """
    Classe TransacaoCommand.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    def __init__(self, transacao_service):
        """
__init__(self, transacao_service)

        Args:
            transacao_service: Descrição do parâmetro.
        """
        self.transacao_service = transacao_service
    
    def executar_transferencia(self, transacao):
        """
executar_transferencia(self, transacao)

        Args:
            transacao: Descrição do parâmetro.
        """
        return self.transacao_service.transferir(transacao)
    
    def executar_deposito(self, transacao):
        """
executar_deposito(self, transacao)

        Args:
            transacao: Descrição do parâmetro.
        """
        return self.transacao_service.depositar(transacao)
    
    def executar_saque(self, transacao):
        """
executar_saque(self, transacao)

        Args:
            transacao: Descrição do parâmetro.
        """
        return self.transacao_service.sacar(transacao)
