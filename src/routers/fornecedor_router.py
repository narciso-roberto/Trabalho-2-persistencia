from fastapi import APIRouter
from dtos.createFornecedorDTO import FornecedorDTO
from services.fornecedor_service import (
    lerFornecedor,
    listarFornecedores,
    cadastrarFornecedor,
    atualizarFornecedor,
    deletarFornecedor,
    buscar_fornecedor_por_nome,
    contar_fornecedores,
)

routerFornecedor = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

@routerFornecedor.get("/")
async def listar_fornecedores(page: int = 1, page_size: int = 10):
    return await listarFornecedores(page, page_size)

@routerFornecedor.get("/quantidade")
async def quantidade_fornecedores():
    return await contar_fornecedores()

@routerFornecedor.get("/buscar")
async def buscar_por_nome(nome: str):
    return await buscar_fornecedor_por_nome(nome)

@routerFornecedor.get("/{id}")
async def ler_fornecedor(id: int):
    return await lerFornecedor(id)

@routerFornecedor.post("")
async def criar_fornecedor(fornecedor: FornecedorDTO):
    return await cadastrarFornecedor(fornecedor)

@routerFornecedor.put("/{id}")
async def atualizar_fornecedor(id: int, fornecedor: FornecedorDTO):
    return await atualizarFornecedor(id, fornecedor)

@routerFornecedor.delete("/{id}")
async def deletar_fornecedor(id: int):
    return await deletarFornecedor(id)
