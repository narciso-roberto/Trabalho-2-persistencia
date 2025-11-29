from sqlmodel import select
from dtos.createProdutoDTO import ProdutoDTO
from database.database import AsyncSessionLocal
from models.produto import Produto
from models.ProdutoTransacaoFornecedor import ProdutoTransacaoFornecedor
from models.fornecedor import Fornecedor
from models.transacao import Transacao
from sqlalchemy import delete, select
from fastapi import Query
from sqlalchemy.orm import joinedload, selectinload
import logging
from datetime import datetime

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


async def produtoPorId(id: int):
    async with AsyncSessionLocal() as session:
        try:
            produto = await session.get(Produto, id)
            if produto is None:
                raise 
            
            return produto
        except Exception as e:
            await session.rollback()
            return (f"Error: {e}")


async def visualizarProdutos(offset: int, limit: int = Query(default=10, le=100)):
    async with AsyncSessionLocal() as session:
        try:
            if offset < 0 or limit < 0:
                raise ValueError("Valor de limite ou offset invalido.")

            statement = select(Produto).offset(offset).limit(limit)
            res = await session.exec(statement)
            return res.scalars().all()
        except Exception as e:
            await session.rollback()
            return (f"Error: {e}")


async def cadastrarProduto(novoProduto: ProdutoDTO):
    async with AsyncSessionLocal() as session:
        try:
            if isIncomplete(novoProduto):
                raise ValueError("O objeto precisa estar totalmente preenchido.")

            novo = Produto(**novoProduto.model_dump())
            session.add(novo)
            await session.commit()
            await session.refresh(novo)
            return novo
        except Exception as e:
            await session.rollback()
            return (f"Error: {e}")


async def deletarProduto(id: int):
    async with AsyncSessionLocal() as session:
        try:
            produtoTransacao = delete(ProdutoTransacaoFornecedor).where(ProdutoTransacaoFornecedor.produto_id == id)
            await session.exec(produtoTransacao)

            deleteProduto = delete(Produto).where(Produto.idProd == id)
            await session.exec(deleteProduto)

            await session.commit()
            return "Produto deletado com sucesso."
        except Exception as e:
            await session.rollback()
            return (f"Error: {e}")


async def atualizarProduto(id: int, atualizadoProduto: ProdutoDTO):
    async with AsyncSessionLocal() as session:
        try:
            ProdutoAlvo = await session.get(Produto, id)
            if ProdutoAlvo is None:
                return "Produto inexistente"

            dados = atualizadoProduto.model_dump(exclude_unset=True)
            for campo, valor in dados.items():
                setattr(ProdutoAlvo, campo, valor)
            session.add(ProdutoAlvo)
            await session.commit()

            return "Produto atualizado com sucesso"
        except Exception as e:
            await session.rollback()
            return (f"Error: {e}")


async def fornecedoresDeProdutos(id: int):
    async with AsyncSessionLocal() as session:
        try:
            produto_obj_res = await session.exec(
                select(Produto).where(Produto.idProd == id).options(
                    joinedload(Produto.transacoesProduto).joinedload(ProdutoTransacaoFornecedor.fornecedor)
                )
            )
            produto_obj = produto_obj_res.scalar_one_or_none()
            if not produto_obj:
                raise ValueError("O Produto nao existe")

            listaTransacoes = produto_obj.transacoesProduto

            listaForn = []
            for x in listaTransacoes:
                if x not in listaForn:
                    listaForn.append(x.fornecedor.nome)

            return listaForn

        except Exception as e:
            await session.rollback()
            return (f"Error: {e}")


async def ProdutosDataTransacoes(dataInicio: str, dataFim: str):

    try:
        dataInicioFormated = datetime.strptime(dataInicio, "%d-%m-%Y").strftime("%Y-%m-%d")
        dataFimFormated = datetime.strptime(dataFim, "%d-%m-%Y").strftime("%Y-%m-%d")
    except Exception:
        return (f"Error: Data formatada incorretamente.")


    async with AsyncSessionLocal() as session:
        try:
            statement = (
                select(Transacao)
                .where(Transacao.data_transacao >= dataInicioFormated, Transacao.data_transacao <= dataFimFormated)
                .options(selectinload(Transacao.itens).joinedload(ProdutoTransacaoFornecedor.produto))
            )

            listaTransacoes_res = await session.exec(statement)
            listaTransacoes = listaTransacoes_res.scalars().all()

            produtos = [
                {"TransacaoID": transacao.transacao_id, "Mercadoria": item.produto.mercadoria, "qtd": transacao.quantidade}
                for transacao in listaTransacoes
                for item in transacao.itens
            ]

            return produtos
        except Exception as e:
            await session.rollback()
            return (f"Error: {e}")


















#UTILITARIOS

def thisExist(sessao, id, objeto):
    obj = sessao.get(objeto, id)

    if obj:
        return 0
    return 1

def isIncomplete(obj):
    dados = obj.model_dump()
    for campo, valor in dados.items():
        if dados[campo] is None:
            return True
    return False


















        