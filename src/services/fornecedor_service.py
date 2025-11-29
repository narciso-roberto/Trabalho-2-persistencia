from sqlmodel import  Session, select
from dtos.createFornecedorDTO import FornecedorDTO
from database.database import engine
from models.fornecedor import Fornecedor
from sqlalchemy import delete

def listarFornecedores(page: int = 1, page_size: int = 10):
    with Session(engine) as session:
        try:
            offset = (page - 1) * page_size
            total = session.exec(select(Fornecedor)).all()
            total_count = len(total)

            query = (
                select(Fornecedor)
                .offset(offset)
                .limit(page_size)
            )
            fornecedores = session.exec(query).all()

            return {
                "page": page,
                "page_size": page_size,
                "total": total_count,
                "total_pages": (total_count + page_size - 1) // page_size,
                "data": fornecedores
            }
        except Exception as error:
            return f"Error: {error}"

def buscar_fornecedor_por_nome(nome: str, limit: int = 20, offset: int = 0):
    with Session(engine) as session:
        try:
            query = (
                select(Fornecedor)
                .where(Fornecedor.nome.ilike(f"%{nome}%"))
                .limit(limit)
                .offset(offset)
            )

            results = session.exec(query).all()
            return results
        except Exception as error:
            return f"Error: {error}"

def lerFornecedor(id: int):
    with Session(engine) as session:
        try:
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