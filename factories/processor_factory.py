
from services.processors.transferencia_processor import TransferenciaProcessor
from services.processors.deposito_processor import DepositoProcessor
from services.processors.saque_processor import SaqueProcessor

class ProcessorFactory:
    @staticmethod
    def criar_processor(tipo, conta_repository, logger):
        if tipo == 'TRANSFERENCIA':
            return TransferenciaProcessor(conta_repository, logger)
        elif tipo == 'DEPOSITO':
            return DepositoProcessor(conta_repository, logger)
        elif tipo == 'SAQUE':
            return SaqueProcessor(conta_repository, logger)
        else:
            raise ValueError(f"Tipo de processor não suportado: {tipo}")
