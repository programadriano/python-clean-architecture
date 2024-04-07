from domain.interfaces.repository import IContasRepository

class ConsultarSaldoUseCase:
    def __init__(self, repo: IContasRepository):
        self.repo = repo

    def execute(self, conta_id: int) -> float:
        conta = self.repo.obter_conta_por_id(conta_id)
        if conta is None:
            raise Exception("Conta não encontrada.")
        return conta.saldo
