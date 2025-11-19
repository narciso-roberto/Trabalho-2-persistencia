from fastapi import APIRouter
from sqlmodel import  Session
from dtos.createProdutoDTO import ProdutoDTO
from models.produto import Produto
from database.database import engine

routerProduto = APIRouter(prefix="/produto")


@routerProduto.post("/cadastrar")
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

@routerProduto.post("/deletar/{id}")
def cadastrarProduto():
    with Session(engine) as session:
        try:
            print("deletar produto..........")
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")

