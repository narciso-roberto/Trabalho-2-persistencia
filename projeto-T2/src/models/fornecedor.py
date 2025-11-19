from sqlmodel import Field, SQLModel

class Fornecedor(SQLModel, table=True):
    idForn: int | None = Field(default=None, primary_key=True)
    cnpj: int
    nome: str
    contato: str
    endereco: str

Fornecedor.model_rebuild()