from sqlmodel import Field, SQLModel, Relationship
from typing import List


class Fornecedor(SQLModel, table=True):
    __tablename__ = "fornecedor"
    idForn: int | None = Field(default=None, primary_key=True)
    cnpj: int
    nome: str
    contato: str
    endereco: str
    transacoesFornecedor: List["ProdutoTransacaoFornecedor"] = Relationship(back_populates="fornecedor")

Fornecedor.model_rebuild()