
from database.database import collection

async def produtoPorId():
    result = await collection.find_one({"name": "joao"})
    print(result)
    return 1


async def visualizarProdutos():
    print()


async def cadastrarProduto():
    print()


async def deletarProduto():
    print()


async def atualizarProduto():
    print()


async def fornecedoresDeProdutos():
    print()


async def ProdutosDataTransacoes():
    print()





































        