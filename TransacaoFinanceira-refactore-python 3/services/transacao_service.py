
from services.logger import Logger

# Open/Closed Principle (OCP) - Aberto para extensão, fechado para modificação
class TransacaoService:
    """
    Classe TransacaoService.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    def __init__(self, conta_repository):
        """
__init__(self, conta_repository)

        Args:
            conta_repository: Descrição do parâmetro.
        """
        self.conta_repository = conta_repository
        self.logger = Logger()
        self.processors = {}

    # Dependency Inversion Principle (DIP) - Depende de abstração
    def registrar_processor(self, tipo, processor):
        """
registrar_processor(self, tipo, processor)

        Args:
            tipo: Descrição do parâmetro.
            processor: Descrição do parâmetro.
        """
        self.processors[tipo] = processor

    # Single Responsibility Principle (SRP) - Responsabilidade de orquestrar o processamento
    def transferir(self, transacao):
        """
transferir(self, transacao)

        Args:
            transacao: Descrição do parâmetro.
        """
        processor = self.processors.get('TRANSFERENCIA')
        
        if not processor:
            self.logger.error('Processor para transferência não encontrado')
            return False

        return processor.processar(transacao)
    
    def depositar(self, transacao):
        """
depositar(self, transacao)

        Args:
            transacao: Descrição do parâmetro.
        """
        processor = self.processors.get('DEPOSITO')
        
        if not processor:
            self.logger.error('Processor para depósito não encontrado')
            return False

        return processor.processar(transacao)
    
    def sacar(self, transacao):
        """
sacar(self, transacao)

        Args:
            transacao: Descrição do parâmetro.
        """
        processor = self.processors.get('SAQUE')
        
        if not processor:
            self.logger.error('Processor para saque não encontrado')
            return False

        return processor.processar(transacao)
