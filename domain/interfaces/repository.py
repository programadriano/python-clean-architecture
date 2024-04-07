from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.conta import Conta

class IContasRepository(ABC):
    @abstractmethod
    def obter_conta_por_id(self, conta_id: int) -> Optional[Conta]:
        pass
