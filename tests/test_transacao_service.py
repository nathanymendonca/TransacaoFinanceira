
import unittest
from unittest.mock import Mock, MagicMock
from models.transacao import Transacao
from models.conta_saldo import ContaSaldo
from services.transacao_service import TransacaoService
from services.processors.transferencia_processor import TransferenciaProcessor

class TestTransacaoService(unittest.TestCase):
    def setUp(self):
        self.mock_conta_repository = Mock()
        self.mock_logger = Mock()
        self.transacao_service = TransacaoService(self.mock_conta_repository)
        
    def test_transferir_com_sucesso(self):
        # Arrange
        conta_origem = ContaSaldo(938485762, 150)
        conta_destino = ContaSaldo(2147483649, 0)
        
        self.mock_conta_repository.get_saldo.side_effect = lambda conta_id: {
            938485762: conta_origem,
            2147483649: conta_destino
        }.get(conta_id)
        
        transferencia_processor = TransferenciaProcessor(self.mock_conta_repository, self.mock_logger)
        self.transacao_service.registrar_processor('TRANSFERENCIA', transferencia_processor)
        
        transacao = Transacao(1, "09/09/2023 14:15:00", 938485762, 2147483649, 100)
        
        # Act
        resultado = self.transacao_service.transferir(transacao)
        
        # Assert
        self.assertTrue(resultado)
        self.assertEqual(conta_origem.saldo, 50)
        self.assertEqual(conta_destino.saldo, 100)
    
    def test_transferir_saldo_insuficiente(self):
        # Arrange
        conta_origem = ContaSaldo(938485762, 50)
        conta_destino = ContaSaldo(2147483649, 0)
        
        self.mock_conta_repository.get_saldo.side_effect = lambda conta_id: {
            938485762: conta_origem,
            2147483649: conta_destino
        }.get(conta_id)
        
        transferencia_processor = TransferenciaProcessor(self.mock_conta_repository, self.mock_logger)
        self.transacao_service.registrar_processor('TRANSFERENCIA', transferencia_processor)
        
        transacao = Transacao(1, "09/09/2023 14:15:00", 938485762, 2147483649, 100)
        
        # Act
        resultado = self.transacao_service.transferir(transacao)
        
        # Assert
        self.assertFalse(resultado)
        self.assertEqual(conta_origem.saldo, 50)  # Saldo não deveria mudar
        self.assertEqual(conta_destino.saldo, 0)  # Saldo não deveria mudar

if __name__ == '__main__':
    unittest.main()
