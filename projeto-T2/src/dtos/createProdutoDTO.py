from sqlmodel import SQLModel

class ProdutoDTO(SQLModel):
    mercadoria: str
    valor: float
    quantidade: int
    categoria: str
