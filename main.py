
from models.transacao import Transacao
from repositories.conta_repository import ContaRepository
from services.transacao_service import TransacaoService
from services.processors.transferencia_processor import TransferenciaProcessor
from services.logger import Logger

def main():
    transacoes = [
        Transacao(1, "09/09/2023 14:15:00", 938485762, 2147483649, 150),
        Transacao(2, "09/09/2023 14:15:05", 2147483649, 210385733, 149),
        Transacao(3, "09/09/2023 14:15:29", 347586970, 238596054, 1100),
        Transacao(4, "09/09/2023 14:17:00", 675869708, 210385733, 5300),
        Transacao(5, "09/09/2023 14:18:00", 238596054, 674038564, 1489),
        Transacao(6, "09/09/2023 14:18:20", 573659065, 563856300, 49),
        Transacao(7, "09/09/2023 14:19:00", 938485762, 2147483649, 44),
        Transacao(8, "09/09/2023 14:19:01", 573659065, 675869708, 150)
    ]

    # Dependency Injection
    logger = Logger()
    conta_repository = ContaRepository()
    transferencia_processor = TransferenciaProcessor(conta_repository, logger)
    
    executor = TransacaoService(conta_repository)
    executor.registrar_processor('TRANSFERENCIA', transferencia_processor)

    for transacao in transacoes:
        executor.transferir(transacao)

if __name__ == "__main__":
    main()
