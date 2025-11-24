from sqlmodel import  Session
from dtos.createFornecedorDTO import FornecedorDTO
from database.database import engine
from models.fornecedor import Fornecedor
from sqlalchemy import delete

def cadastrarFornecedor(novoFornecedor: FornecedorDTO):
    with Session(engine) as session:
        try:
            new = Produto(**novoFornecedor.model_dump())
            session.add(new)
            session.commit()
            return new
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