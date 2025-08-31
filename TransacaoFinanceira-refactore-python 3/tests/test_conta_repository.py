
import unittest
from models.conta_saldo import ContaSaldo
from repositories.conta_repository import ContaRepository

class TestContaRepository(unittest.TestCase):
    """
    Classe TestContaRepository.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    def setUp(self):
        """
setUp(self)

        Args:
        """
        self.repository = ContaRepository()
    
    def test_get_saldo_conta_existente(self):
        """
test_get_saldo_conta_existente(self)

        Args:
        """
        # Arrange
        conta_id = 938485762
        
        # Act
        conta_saldo = self.repository.get_saldo(conta_id)
        
        # Assert
        self.assertIsNotNone(conta_saldo)
        self.assertEqual(conta_saldo.conta_id, conta_id)
        self.assertEqual(conta_saldo.saldo, 180)
    
    def test_get_saldo_conta_inexistente(self):
        """
test_get_saldo_conta_inexistente(self)

        Args:
        """
        # Arrange
        conta_id = 999999999
        
        # Act
        conta_saldo = self.repository.get_saldo(conta_id)
        
        # Assert
        self.assertIsNone(conta_saldo)
    
    def test_atualizar_saldo_conta_existente(self):
        """
test_atualizar_saldo_conta_existente(self)

        Args:
        """
        # Arrange
        conta_saldo = ContaSaldo(938485762, 500)
        
        # Act
        resultado = self.repository.atualizar_saldo(conta_saldo)
        conta_atualizada = self.repository.get_saldo(938485762)
        
        # Assert
        self.assertTrue(resultado)
        self.assertEqual(conta_atualizada.saldo, 500)
    
    def test_atualizar_saldo_nova_conta(self):
        """
test_atualizar_saldo_nova_conta(self)

        Args:
        """
        # Arrange
        nova_conta = ContaSaldo(999999999, 1000)
        
        # Act
        resultado = self.repository.atualizar_saldo(nova_conta)
        conta_criada = self.repository.get_saldo(999999999)
        
        # Assert
        self.assertTrue(resultado)
        self.assertIsNotNone(conta_criada)
        self.assertEqual(conta_criada.saldo, 1000)

if __name__ == '__main__':
    unittest.main()
