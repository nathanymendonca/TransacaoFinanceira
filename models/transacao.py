
from datetime import datetime

class Transacao:
    def __init__(self, correlation_id, data_hora, conta_origem, conta_destino, valor):
        self.correlation_id = correlation_id
        self.data_hora = datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.valor = valor
