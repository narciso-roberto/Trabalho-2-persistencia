from sqlmodel import SQLModel

class Fornecedor(SQLModel):
    cnpj: int
    nome: str
    contato: str
    endereco: str
