
from interfaces.i_transacao_processor import ITransacaoProcessor

# Single Responsibility Principle (SRP) - Responsabilidade específica para transferência
class TransferenciaProcessor(ITransacaoProcessor):
    """
    Classe TransferenciaProcessor.

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
            self.logger.log(f"Transacao numero {transacao.correlation_id} foi cancelada por falta de saldo")
            return False

        conta_saldo_destino = self.conta_repository.get_saldo(transacao.conta_destino)
        
        if not conta_saldo_destino:
            self.logger.log(f"Conta destino {transacao.conta_destino} não encontrada")
            return False

        conta_saldo_origem.saldo -= transacao.valor
        conta_saldo_destino.saldo += transacao.valor

        self.conta_repository.atualizar_saldo(conta_saldo_origem)
        self.conta_repository.atualizar_saldo(conta_saldo_destino)

        self.logger.log(f"Transacao numero {transacao.correlation_id} foi efetivada com sucesso! Novos saldos: Conta Origem: {conta_saldo_origem.saldo} | Conta Destino: {conta_saldo_destino.saldo}")
        return True
