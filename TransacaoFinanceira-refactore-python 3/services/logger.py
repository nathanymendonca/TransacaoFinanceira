
from datetime import datetime

class Logger:
    """
    Classe Logger.

    Attributes:
        # Adicione aqui os atributos relevantes da classe.
    """
    def log(self, message):
        """
log(self, message)

        Args:
            message: Descrição do parâmetro.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    
    def error(self, message):
        """
error(self, message)

        Args:
            message: Descrição do parâmetro.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ERROR: {message}")
