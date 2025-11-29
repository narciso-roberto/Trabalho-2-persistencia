from sqlmodel import  Session
from src.dtos.createProdutoDTO import ProdutoDTO
from src.database.database import engine
from src.models.produto import Produto
from src.models.ProdutoTransacaoFornecedor import ProdutoTransacaoFornecedor
from src.models.fornecedor import Fornecedor
from src.models.transacao import Transacao
from sqlalchemy import delete,select
from fastapi import Query
from sqlalchemy.orm import joinedload, selectinload
import logging
from datetime import datetime
#Verificar se os produtos nao estao vazios

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)



def produtoPorId(id: int):
    with Session(engine) as session:
        try:
            stmt = (
            select(Produto)
            .options(selectinload(Produto.transacoesProduto).selectinload(ProdutoTransacaoFornecedor.fornecedor),
            selectinload(Produto.transacoesProduto).selectinload(ProdutoTransacaoFornecedor.transacao) 
            ).where(Produto.idProd == id)
            
            )
            produto = session.scalar(stmt)
            return produto
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")

def visualizarProdutos(offset: int, limit:int = Query(default=10,le=100)):
    with Session(engine) as session:
        try:
            if offset < 0 or limit < 0:
                raise ValueError("Valor de limite ou offset invalido.")
            
            statement = select(Produto).offset(offset).limit(limit)
            return session.scalars(statement).all()
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")

def cadastrarProduto(novoProduto: ProdutoDTO):
    with Session(engine) as session:
        try:
            if isIncomplete(novoProduto):
                raise ValueError("O objeto precisa estar totalmente preenchido.")
            
            novo = Produto(**novoProduto.model_dump())
            session.add(novo)
            # session.commit()
            return novo
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")
        
def deletarProduto(id: int):
    with Session(engine) as session:
        try:

            # apagando transacoes do produto
            produtoTransacao = delete(ProdutoTransacaoFornecedor).where(ProdutoTransacaoFornecedor.produto_id == id) 
            session.exec(produtoTransacao)
            

            # apagando produto
            deleteProduto = delete(Produto).where(Produto.idProd == id) 
            session.exec(deleteProduto)

            session.commit()
            return "Produto deletado com sucesso."
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")

def atualizarProduto(id: int, atualizadoProduto: ProdutoDTO):
    with Session(engine) as session:
        
        try:
            ProdutoAlvo = session.get(Produto, id)
            session.add(ProdutoAlvo)

            dados = atualizadoProduto.model_dump(exclude_unset=True)
            for campo, valor in dados.items():
                setattr(ProdutoAlvo, campo, valor)
            session.add(ProdutoAlvo)
            session.commit()
            
            return "Produto atualizado com sucesso"
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")

def fornecedoresDeProdutos(id: int):
    with Session(engine) as session:
        try:

            if thisExist(session,id,Produto):
                raise ValueError("O Produto nao existe")

            statement = (
                select(Produto).where(Produto.idProd == id)
                .options(
                    joinedload(Produto.transacoesProduto).
                    joinedload(ProdutoTransacaoFornecedor.fornecedor),
                    
                )
            )

            listaTransacoes = session.scalar(statement).transacoesProduto

            listaForn = []
            for x in listaTransacoes:
                if x not in listaForn:
                    listaForn.append(x.fornecedor.nome)

            return listaForn
        

        except Exception as e:
            session.rollback()
            return(f"Error: {e}")

def ProdutosDataTransacoes(dataInicio: str, dataFim: str):

    try:
        dataInicioFormated = datetime.strptime(dataInicio, "%d-%m-%Y").strftime("%Y-%m-%d")
        dataFimFormated = datetime.strptime(dataFim, "%d-%m-%Y").strftime("%Y-%m-%d")
    except Exception as e:
        # TRATAR MELHOR ESSES ERROS
        return(f"Error: Data formatada incorretamente.")

    
    with Session(engine) as session:
        try:
            statement = (
                select(Transacao).
                where(Transacao.data_transacao >= dataInicioFormated, 
                    Transacao.data_transacao <= dataFimFormated).
                    options(selectinload(Transacao.itens).
                    joinedload(ProdutoTransacaoFornecedor.produto))
                    
            )

            listaTransacoes = session.scalars(statement).all()

            
            produtos = [
                {"TransacaoID": transacao.transacao_id, "Mercadoria":item.produto.mercadoria, "qtd": transacao.quantidade}
                for transacao in listaTransacoes
                for item in transacao.itens
            ]
            
        
            return produtos
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")


















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


















        