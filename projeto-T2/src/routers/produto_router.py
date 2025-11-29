from fastapi import APIRouter
from src.dtos.createProdutoDTO import ProdutoDTO
from src.services import produto_service as service
from src.models.produto import ProdutoResponse

routerProduto = APIRouter(prefix="/produto")

@routerProduto.get("/ProdutoPorId/{id}", response_model=ProdutoResponse)
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
