from domain.interfaces.repository import IContasRepository

class ContasRepository(IContasRepository):
    def obter_saldo(self, conta_id) -> float:
        # Aqui iria a lógica para acessar o banco de dados e retornar o saldo
        return 100.0  
