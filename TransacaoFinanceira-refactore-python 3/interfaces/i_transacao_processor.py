
from abc import ABC, abstractmethod

# Interface Segregation Principle (ISP)
class ITransacaoProcessor(ABC):
    """
    Classe ITransacaoProcessor.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    @abstractmethod
    def processar(self, transacao):
        """
processar(self, transacao)

        Args:
            transacao: Descrição do parâmetro.
        """
        pass
