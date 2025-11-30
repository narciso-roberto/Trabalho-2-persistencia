from sqlmodel import Field, SQLModel, Relationship


class Produto(SQLModel, table=True):
    __tablename__ = "produto"
    idProd: int | None = Field(default=None, primary_key=True)
    mercadoria: str
    valor: float
    quantidade: int
    categoria: str
    transacoesProduto: list["ProdutoTransacaoFornecedor"] = Relationship(back_populates="produto")

Produto.model_rebuild()





