from sqlmodel import  Session
from dtos.createProdutoDTO import ProdutoDTO
from database.database import engine
from models.produto import Produto
from models.ProdutoTransacaoFornecedor import ProdutoTransacaoFornecedor
from models.fornecedor import Fornecedor
from sqlalchemy import delete,select
from fastapi import Query
from sqlalchemy.orm import joinedload
#Verificar se os produtos nao estao vazios

def produtoPorId(id: int):
    with Session(engine) as session:
        try:
            produto = session.get(Produto,id)
            if produto is None:
                return "Produto inexistente"
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
            statement = select(Produto).where(Produto.idProd == 7).options(joinedload(Produto.transacoesProduto))
            return session.scalars(statement).unique().all()[0].transacoesProduto
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")


















#UTILITARIOS

def isIncomplete(obj):
    dados = obj.model_dump()
    for campo, valor in dados.items():
        if dados[campo] is None:
            return True
    return False


















        