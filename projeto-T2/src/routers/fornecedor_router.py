from fastapi import APIRouter
from dtos.createFornecedorDTO import FornecedorDTO
from services.fornecedor_service import (
    lerFornecedor,
    cadastrarFornecedor,
    atualizarFornecedor,
    deletarFornecedor
)

routerFornecedor = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

@routerFornecedor.get("/{id}")
def ler_fornecedor(id: int):
    return lerFornecedor(id)

@routerFornecedor.post("")
def criar_fornecedor(fornecedor: FornecedorDTO):
    return cadastrarFornecedor(fornecedor)

@routerFornecedor.put("/{id}")
def atualizar_fornecedor(id: int, fornecedor: FornecedorDTO):
    return atualizarFornecedor(id, fornecedor)

@routerFornecedor.delete("/{id}")
def deletar_fornecedor(id: int):
    return deletarFornecedor(id)
