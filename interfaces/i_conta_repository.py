
from abc import ABC, abstractmethod

class IContaRepository(ABC):
    @abstractmethod
    def get_saldo(self, conta_id):
        pass
    
    @abstractmethod
    def atualizar_saldo(self, conta_saldo):
        pass
