from fastapi import APIRouter
from dtos.createProdutoDTO import ProdutoDTO
from services import produto_service as service
from models.produto import ProdutoResponse

routerProduto = APIRouter(prefix="/produto", tags=["Produto"])

@routerProduto.get("/ProdutoPorId/{id}", response_model=ProdutoResponse)
async def produtoPorId(id: int):
    """
    Obtém um produto pelo ID.

    Args:\n
        id (int): ID do produto

    Returns:\n
        idProd: ID do produto\n
        mercadoria: Nome da mercadoria\n
        valor: Valor unitário\n
        quantidade: Quantidade em estoque\n
        categoria: Categoria do produto
    """
    return await service.produtoPorId(id)

@routerProduto.get("/visualizar/{pagina}/{qtd}")
async def visualizarProduto(pagina: int, qtd: int):
    """
    Obtém a lista de produtos com paginação.

    Args:\n
        pagina (int): Número da página\n
        qtd (int): Quantidade de produtos por página

    Returns:\n
        Lista de produtos paginada
    """
    return await service.visualizarProdutos(pagina, qtd)

@routerProduto.get("/fornecedoresDeProdutos/{id}")
async def fornecedoresDeProdutos(id: int, offset: int = 0):
    """
    Obtém a lista de fornecedores de um produto específico.

    Args:\n
        id (int): ID do produto\n
        offset (int): Deslocamento opcional

    Returns:\n
        Lista de nomes de fornecedores que fornecem este produto
    """
    return await service.fornecedoresDeProdutos(id, offset)

@routerProduto.get("/produtosDataTransacoes")
async def atualizarProduto(dataInicio: str, dataFim: str, offset: int = 0):
    """
    Obtém produtos com transações dentro de um período de datas.

    Args:\n
        dataInicio (str): Data inicial no formato DD-MM-YYYY\n
        dataFim (str): Data final no formato DD-MM-YYYY\n
        offset (int): Deslocamento opcional

    Returns:\n
        Lista de produtos e suas transações no período especificado
    """
    return await service.ProdutosDataTransacoes(dataInicio, dataFim, offset)

@routerProduto.post("/cadastrar")
async def cadastrarProduto(novoProduto: ProdutoDTO):
    """
    Cadastra um novo produto.

    Args:\n
        mercadoria (str): Nome da mercadoria\n
        valor (float): Valor unitário\n
        quantidade (int): Quantidade inicial\n
        categoria (str): Categoria do produto

    Returns:\n
        Produto cadastrado com sucesso
    """
    return await service.cadastrarProduto(novoProduto)

@routerProduto.delete("/deletar/{id}")
async def deletarProduto(id: int):
    """
    Deleta um produto pelo ID.

    Args:\n
        id (int): ID do produto a deletar

    Returns:\n
        Mensagem de sucesso ou erro
    """
    return await service.deletarProduto(id)

@routerProduto.put("/atualizar/{id}")
async def atualizarProduto(id: int, atualizadoProduto: ProdutoDTO):
    """
    Atualiza um produto existente.

    Args:\n
        id (int): ID do produto\n
        mercadoria (str): Nova mercadoria (opcional)\n
        valor (float): Novo valor (opcional)\n
        quantidade (int): Nova quantidade (opcional)\n
        categoria (str): Nova categoria (opcional)

    Returns:\n
        Produto atualizado com sucesso
    """
    return await service.atualizarProduto(id, atualizadoProduto)
