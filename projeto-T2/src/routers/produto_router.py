from fastapi import APIRouter
# from sqlmodel import  Session
from src.dtos.createProdutoDTO import ProdutoDTO
# from database.database import engine
# from models.produto import Produto
# from models.produtoFornecedor import ProdutoFornecedor
# from models.transacao import Transacao
# from sqlalchemy import select, delete


from src.services import produto_service as service


routerProduto = APIRouter(prefix="/produto", tags=["Produto"])

@routerProduto.get("/ProdutoPorId/{id}")
def produtoPorId(id:int):
    return service.produtoPorId(id)

@routerProduto.get("/visualizar/{pagina}/{qtd}")
def visualizarProduto(pagina: int, qtd:int):
    return service.visualizarProdutos(pagina,qtd)

@routerProduto.get("/fornecedoresDeProdutos/{id}")
def fornecedoresDeProdutos(id: int):
    return service.fornecedoresDeProdutos(id)

@routerProduto.get("/produtosDataTransacoes")
def atualizarProduto(dataInicio: str, dataFim: str):
    return service.ProdutosDataTransacoes(dataInicio,dataFim)

@routerProduto.post("/cadastrar")
def cadastrarProduto(novoProduto: ProdutoDTO):
    return service.cadastrarProduto(novoProduto)

@routerProduto.delete("/deletar/{id}")
def deletarProduto(id: int):
    return service.deletarProduto(id)

@routerProduto.put("/atualizar/{id}")
def atualizarProduto(id: int, atualizadoProduto: ProdutoDTO):
    return service.atualizarProduto(id, atualizadoProduto)
