
from abc import ABC, abstractmethod

class IContaRepository(ABC):
    """
    Classe IContaRepository.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    @abstractmethod
    def get_saldo(self, conta_id):
        """
get_saldo(self, conta_id)

        Args:
            conta_id: Descrição do parâmetro.
        """
        pass
    
    @abstractmethod
    def atualizar_saldo(self, conta_saldo):
        """
atualizar_saldo(self, conta_saldo)

        Args:
            conta_saldo: Descrição do parâmetro.
        """
        pass
