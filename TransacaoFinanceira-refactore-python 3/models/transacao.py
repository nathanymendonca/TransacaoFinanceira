
from datetime import datetime

class Transacao:
    """
    Classe Transacao.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    def __init__(self, correlation_id, data_hora, conta_origem, conta_destino, valor):
        """
__init__(self, correlation_id, data_hora, conta_origem, conta_destino, valor)

        Args:
            correlation_id: Descrição do parâmetro.
            data_hora: Descrição do parâmetro.
            conta_origem: Descrição do parâmetro.
            conta_destino: Descrição do parâmetro.
            valor: Descrição do parâmetro.
        """
        self.correlation_id = correlation_id
        self.data_hora = datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.valor = valor
