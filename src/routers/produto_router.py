from fastapi import APIRouter
from src.dtos.createProdutoDTO import ProdutoDTO
from src.services import produto_service as service
from src.models.produto import ProdutoResponse

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
