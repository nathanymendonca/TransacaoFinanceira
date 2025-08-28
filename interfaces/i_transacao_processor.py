
from abc import ABC, abstractmethod

# Interface Segregation Principle (ISP)
class ITransacaoProcessor(ABC):
    @abstractmethod
    def processar(self, transacao):
        pass
