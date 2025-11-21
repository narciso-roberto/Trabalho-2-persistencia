from sqlmodel import  Session
from dtos.createProdutoDTO import ProdutoDTO
from database.database import engine
from models.produto import Produto
from models.ProdutoTransacaoFornecedor import ProdutoTransacaoFornecedor
from sqlalchemy import delete


def cadastrarProduto(novoProduto: ProdutoDTO):
    with Session(engine) as session:
        try:
            novo = Produto(**novoProduto.model_dump())
            session.add(novo)
            session.commit()
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
        






















        