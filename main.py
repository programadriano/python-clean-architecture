from application.use_cases.consultar_saldo import ConsultarSaldoUseCase
from fastapi import FastAPI, HTTPException
from adapters.repository.contas_repository import ContasRepositoryMemoria
from infrastructure.logging.logging_config import setup_logging
import logging

app = FastAPI()
contas_repo = ContasRepositoryMemoria()

setup_logging()
logger = logging.getLogger(__name__)

@app.get("/contas/{conta_id}/saldo")
def consultar_saldo(conta_id: int):
    logger.info(f'Iniciando consulta de saldo para conta {conta_id}')
    use_case = ConsultarSaldoUseCase(contas_repo)
    try:
        saldo = use_case.execute(conta_id)
        logger.info(f'Saldo consultado para conta {conta_id}: {saldo}')
        return {"conta_id": conta_id, "saldo": saldo}
    except Exception as e:
        logger.error(f'Erro ao consultar saldo para conta {conta_id}: {e}', exc_info=True)
        raise HTTPException(status_code=404, detail=str(e))
