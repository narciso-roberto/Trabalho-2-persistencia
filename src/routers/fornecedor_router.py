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
    ordenar_fornecedores_por_nome
)

routerFornecedor = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

@routerFornecedor.get("/")
async def listar_fornecedores(page: int = 1, page_size: int = 10):
    """
    Obtém a lista de fornecedores por paginação.

    Args:\n
        page (int): Número da página \n
        page_size (int): Tamanho da página

    Returns:\n
        page: Página atual\n
        page_size: Tamanho da página\n
        total: quantidade de fornecedores\n
        total_pages: quantidade de páginas pelo tamanho\n
        data: lista de fornecedores
    """
    return await listarFornecedores(page, page_size)

@routerFornecedor.get("/quantidade")
async def quantidade_fornecedores():
    """
    Obtém a quantidade de fornecedores cadastrados.

    Args:\n
        Nenhum

    Returns:\n
        number: quantidade de fornecedores
    """
    return await contar_fornecedores()

@routerFornecedor.get("/ordenacao")
async def ordenacao_fornecedores():
    """
    Obtém a lista de fornecedores ordenado por nome.

    Args:\n
        Nenhum

    Returns:\n
        list: Lista de fornecedores ordenados por nome.
    """
    return await ordenar_fornecedores_por_nome()

@routerFornecedor.get("/buscar")
async def buscar_por_nome(nome: str):
    """
    Busca de fornecedores por string.

    Args:\n
        nome (str): nome completo ou parcial do fornecedor.

    Returns:\n
        list: resultado da busca pela string.
    """
    return await buscar_fornecedor_por_nome(nome)

@routerFornecedor.get("/{id}")
async def ler_fornecedor(id: int):
    """
    Busca de fornecedor por id.

    Args:\n
        id (int): id do fornecedor.

    Returns:\n
        fornecedor: resultado do fornecedor com id informado.
    """
    return await lerFornecedor(id)

@routerFornecedor.post("")
async def criar_fornecedor(fornecedor: FornecedorDTO):
    """
    Criar novo fornecedor

    Body:\n
        cnpj (int): cnpj da empresa
        nome (str): nome da empresa
        contato (str): telefone do fornecedor
        endereco (str): Rua/cidade do fornecedor

    Returns:\n
        Fornecedor: resultado do fornecedor criado com idForn
    """
    return await cadastrarFornecedor(fornecedor)

@routerFornecedor.put("/{id}")
async def atualizar_fornecedor(id: int, fornecedor: FornecedorDTO):
    """
    Atualizar fornecedor.

    Args:\n
        id (int): idForn do fornecedor alvo.
    
    Body:\n
        cnpj (int): cnpj da empresa
        nome (str): nome da empresa
        contato (str): telefone do fornecedor
        endereco (str): Rua/cidade do fornecedo

    Returns:\n
        Fornecedor: resultado da atualização
    """
    return await atualizarFornecedor(id, fornecedor)

@routerFornecedor.delete("/{id}")
async def deletar_fornecedor(id: int):
    """
    Deletar fornecedor.

    Args:\n
        id (int): idForn do fornecedor alvo.

    Returns:\n
        str: Fornecedor deletado com sucesso.
    """
    return await deletarFornecedor(id)
