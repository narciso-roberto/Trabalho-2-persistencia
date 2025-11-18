from fastapi import APIRouter
from sqlmodel import  Session
from dtos.createProdutoDTO import Produto
from database.database import engine

router = APIRouter(prefix="/produto")


@router.post("/cadastrar")
def cadastrarProduto(novoProduto: Produto):
    with Session(engine) as engine:
        try:
            print("criar produto")
        except:
            print("a")

@router.post("/deletar/{id}")
def cadastrarProduto():
    with Session(engine) as engine:
        try:
            print("deletar produto")
        except:
            print("a")

