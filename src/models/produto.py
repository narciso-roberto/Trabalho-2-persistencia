from sqlmodel import Field, SQLModel, Relationship
from typing import List

from .ProdutoTransacaoFornecedor import PTFResponse

class Produto(SQLModel, table=True):
    __tablename__ = "produto"
    idProd: int | None = Field(default=None, primary_key=True)
    mercadoria: str
    valor: float
    quantidade: int
    categoria: str
    transacoesProduto: list["ProdutoTransacaoFornecedor"] = Relationship(back_populates="produto")

class ProdutoResponse(SQLModel):
    model_config = {"from_attributes": True}

    mercadoria: str
    valor: float
    quantidade: int
    categoria: str
    transacoesProduto: List[PTFResponse] = []

Produto.model_rebuild()





