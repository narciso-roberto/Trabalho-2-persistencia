from sqlmodel import Field, SQLModel, Relationship
from typing import List

class Produto(SQLModel, table=True):
    idProd: int | None = Field(default=None, primary_key=True)
    mercadoria: str
    valor: float
    quantidade: int
    categoria: str
    transacoesProduto: list["ProdutoTransacaoFornecedor"] = Relationship(back_populates="produto")



from src.models.ProdutoTransacaoFornecedor import PTFResponse

class ProdutoResponse(SQLModel):
    model_config = {"from_attributes": True}

    mercadoria: str
    valor: float
    quantidade: int
    categoria: str
    transacoesProduto: List[PTFResponse] = []

Produto.model_rebuild()





