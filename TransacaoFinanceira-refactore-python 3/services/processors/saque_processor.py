
from interfaces.i_transacao_processor import ITransacaoProcessor

class SaqueProcessor(ITransacaoProcessor):
    """
    Classe SaqueProcessor.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    def __init__(self, conta_repository, logger):
        """
__init__(self, conta_repository, logger)

        Args:
            conta_repository: Descrição do parâmetro.
            logger: Descrição do parâmetro.
        """
        self.conta_repository = conta_repository
        self.logger = logger

    def processar(self, transacao):
        """
processar(self, transacao)

        Args:
            transacao: Descrição do parâmetro.
        """
        conta_saldo_origem = self.conta_repository.get_saldo(transacao.conta_origem)
        
        if not conta_saldo_origem:
            self.logger.log(f"Conta origem {transacao.conta_origem} não encontrada")
            return False
        
        if conta_saldo_origem.saldo < transacao.valor:
            self.logger.log(f"Saque numero {transacao.correlation_id} foi cancelado por falta de saldo")
            return False

        conta_saldo_origem.saldo -= transacao.valor
        self.conta_repository.atualizar_saldo(conta_saldo_origem)

        self.logger.log(f"Saque numero {transacao.correlation_id} foi efetivado com sucesso! Novo saldo: {conta_saldo_origem.saldo}")
        return True
