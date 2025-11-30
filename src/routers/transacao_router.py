from fastapi import APIRouter, Query

from dtos.createTransacaoDTO import CreateTransacaoDTO
from dtos.updateTransacaoDTO import UpdateTransacaoDTO
from dtos.transacaoRespostaDTO import TransacaoRespostaDTO
from dtos.pagination import Pagination 

from services.transacao_service import resgatarTodas, resgatarUm, criar, atualizar, deletar

from datetime import datetime

router = APIRouter(prefix="/transacao", tags=["Transação"])

@router.get("/")
def listar_transacoes(offset: int = Query(default=1), limit: int = Query(default=10), data_inicial: datetime | None = Query(default=None), data_final: datetime | None = Query(default=None)) -> Pagination[TransacaoRespostaDTO] | str:
    if offset < 1 or limit < 1:
        return "Offset e limit devem ser maiores ou iguais a 0."
    
    offset = (offset - 1) * limit
    
    return resgatarTodas(offset, limit, data_inicial, data_final)

@router.get("/{id}")
def obter_transacao(id: int):
    return resgatarUm(id)

@router.post("/")
def criar_transacao(novaTransacao: CreateTransacaoDTO):
    return criar(novaTransacao)

@router.put("/{id}")
def atualizar_transacao(id: int, transacaoAtualizada: UpdateTransacaoDTO):
    return atualizar(id, transacaoAtualizada)

@router.delete("/{id}")
def deletar_transacao(id: int):
    return deletar(id)