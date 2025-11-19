from sqlmodel import Field, SQLModel


class Produto(SQLModel, table=True):
    idProd: int | None = Field(default=None, primary_key=True)
    mercadoria: str
    valor: float
    quantidade: int
    categoria: str

Produto.model_rebuild()





