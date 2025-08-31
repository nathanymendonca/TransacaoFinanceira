
from services.processors.transferencia_processor import TransferenciaProcessor
from services.processors.deposito_processor import DepositoProcessor
from services.processors.saque_processor import SaqueProcessor

class ProcessorFactory:
    """
    Classe ProcessorFactory.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    @staticmethod
    def criar_processor(tipo, conta_repository, logger):
        """
criar_processor(tipo, conta_repository, logger)

        Args:
            tipo: Descrição do parâmetro.
            conta_repository: Descrição do parâmetro.
            logger: Descrição do parâmetro.
        """
        if tipo == 'TRANSFERENCIA':
            return TransferenciaProcessor(conta_repository, logger)
        elif tipo == 'DEPOSITO':
            return DepositoProcessor(conta_repository, logger)
        elif tipo == 'SAQUE':
            return SaqueProcessor(conta_repository, logger)
        else:
            raise ValueError(f"Tipo de processor não suportado: {tipo}")
