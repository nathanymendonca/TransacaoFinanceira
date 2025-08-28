
from services.logger import Logger

# Open/Closed Principle (OCP) - Aberto para extensão, fechado para modificação
class TransacaoService:
    def __init__(self, conta_repository):
        self.conta_repository = conta_repository
        self.logger = Logger()
        self.processors = {}

    # Dependency Inversion Principle (DIP) - Depende de abstração
    def registrar_processor(self, tipo, processor):
        self.processors[tipo] = processor

    # Single Responsibility Principle (SRP) - Responsabilidade de orquestrar o processamento
    def transferir(self, transacao):
        processor = self.processors.get('TRANSFERENCIA')
        
        if not processor:
            self.logger.error('Processor para transferência não encontrado')
            return False

        return processor.processar(transacao)
    
    def depositar(self, transacao):
        processor = self.processors.get('DEPOSITO')
        
        if not processor:
            self.logger.error('Processor para depósito não encontrado')
            return False

        return processor.processar(transacao)
    
    def sacar(self, transacao):
        processor = self.processors.get('SAQUE')
        
        if not processor:
            self.logger.error('Processor para saque não encontrado')
            return False

        return processor.processar(transacao)
