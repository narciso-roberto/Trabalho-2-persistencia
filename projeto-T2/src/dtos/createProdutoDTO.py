from sqlmodel import SQLModel, Field

class ProdutoDTO(SQLModel):
    mercadoria: str | None = Field(default=None)
    valor: float | None = Field(default=None)
    quantidade: int | None = Field(default=None)
    categoria: str | None = Field(default=None)
