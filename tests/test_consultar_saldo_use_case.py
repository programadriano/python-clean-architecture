# tests/test_consultar_saldo_use_case.py
from domain.use_cases.consultar_saldo import ConsultarSaldoUseCase
import pytest
from unittest.mock import Mock
from domain.entities.conta import Conta
from domain.interfaces.repository import IContasRepository

def test_consultar_saldo_use_case_sucesso():
    # Mock do repositório
    repo = Mock(IContasRepository)
    conta_teste = Conta(id=1, saldo=100.0)
    repo.obter_conta_por_id.return_value = conta_teste
    
    # Inicialização do caso de uso com o repositório mockado
    use_case = ConsultarSaldoUseCase(repo)
    
    # Execução
    resultado = use_case.execute(conta_id=1)
    
    # Verificações
    repo.obter_conta_por_id.assert_called_once_with(1)
    assert resultado == 100.0

def test_consultar_saldo_use_case_falha_conta_nao_encontrada():
    # Mock do repositório para simular uma conta não encontrada
    repo = Mock(IContasRepository)
    repo.obter_conta_por_id.return_value = None
    
    # Inicialização do caso de uso com o repositório mockado
    use_case = ConsultarSaldoUseCase(repo)
    
    # Execução e verificação da exceção
    with pytest.raises(Exception):
        use_case.execute(conta_id=999)
