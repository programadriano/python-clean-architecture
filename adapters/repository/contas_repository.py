from domain.interfaces.repository import IContasRepository
from domain.entities.conta import Conta

class ContasRepositoryMemoria(IContasRepository):
    _contas = {1: Conta(1, 100.0), 2: Conta(2, 250.0)}

    def obter_conta_por_id(self, conta_id: int) -> Conta:
        return self._contas.get(conta_id)
