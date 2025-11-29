from fastapi import APIRouter
from dtos.createFornecedorDTO import FornecedorDTO
from services.fornecedor_service import (
    lerFornecedor,
    listarFornecedores,
    cadastrarFornecedor,
    atualizarFornecedor,
    deletarFornecedor,
    buscar_fornecedor_por_nome
)

routerFornecedor = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

@routerFornecedor.get("/")
def listar_fornecedores(page: int = 1, page_size: int = 10):
    return listarFornecedores(page, page_size)

@routerFornecedor.get("/buscar")
def buscar_por_nome(nome: str):
    return buscar_fornecedor_por_nome(nome)

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
