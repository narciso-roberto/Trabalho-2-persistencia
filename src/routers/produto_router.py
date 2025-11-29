from fastapi import APIRouter
# from sqlmodel import  Session
from dtos.createProdutoDTO import ProdutoDTO
# from database.database import engine
# from models.produto import Produto
# from models.produtoFornecedor import ProdutoFornecedor
# from models.transacao import Transacao
# from sqlalchemy import select, delete


from services import produto_service as service


routerProduto = APIRouter(prefix="/produto", tags=["Produto"])

@routerProduto.get("/ProdutoPorId/{id}")
async def produtoPorId(id:int):
    return await service.produtoPorId(id)

@routerProduto.get("/visualizar/{pagina}/{qtd}")
async def visualizarProduto(pagina: int, qtd:int):
    return await service.visualizarProdutos(pagina,qtd)

@routerProduto.get("/fornecedoresDeProdutos/{id}")
async def fornecedoresDeProdutos(id: int):
    return await service.fornecedoresDeProdutos(id)

@routerProduto.get("/produtosDataTransacoes")
async def atualizarProduto(dataInicio: str, dataFim: str):
    return await service.ProdutosDataTransacoes(dataInicio,dataFim)

@routerProduto.post("/cadastrar")
async def cadastrarProduto(novoProduto: ProdutoDTO):
    return await service.cadastrarProduto(novoProduto)

@routerProduto.delete("/deletar/{id}")
async def deletarProduto(id: int):
    return await service.deletarProduto(id)

@routerProduto.put("/atualizar/{id}")
async def atualizarProduto(id: int, atualizadoProduto: ProdutoDTO):
    return await service.atualizarProduto(id, atualizadoProduto)
