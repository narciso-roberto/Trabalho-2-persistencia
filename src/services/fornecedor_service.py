from sqlmodel import  Session
from dtos.createFornecedorDTO import FornecedorDTO
from database.database import engine
from models.fornecedor import Fornecedor
from sqlalchemy import delete

def lerFornecedor(id: int):
    try:
        with Session(engine) as session:
            fornecedor = session.get(Fornecedor, id)
            if not fornecedor:
                return f"Fornecedor com id {id} não encontrado."
            
            return fornecedor
    except Exception as error:
        return f"Error: {error}"


def cadastrarFornecedor(novoFornecedor: FornecedorDTO):
    with Session(engine) as session:
        try:
            new = Fornecedor(**novoFornecedor.model_dump())
            session.add(new)
            session.commit()
            return new
        except Exception as error:
            session.rollback()
            return(f"Error: {error}")

def atualizarFornecedor(id: int, newData: FornecedorDTO):
    with Session(engine) as session:
        try:
            fornecedor = session.get(Fornecedor, id)
            if not fornecedor:
                return "Fornecedor com id {id} não encontrado."

            for chave, valor in newData.model_dump().items():
                setattr(fornecedor, chave, valor)

            session.add(fornecedor)
            session.commit()
            session.refresh(fornecedor)

            return fornecedor
        except Exception as error:
            session.rollback()
            return(f"Error: {error}")

def deletarFornecedor(id: int):
    with Session(engine) as session:
        try:
            deletedFornecedor = delete(Fornecedor).where(Fornecedor.idForn == id) 
            session.exec(deletedFornecedor)
            session.commit()

            return "Fornecedor deletado com sucesso."
        except Exception as error:
            session.rollback()
            return(f"Error: {error}")