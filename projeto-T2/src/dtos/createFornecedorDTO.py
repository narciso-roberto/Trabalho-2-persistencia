from sqlmodel import SQLModel

class FornecedorDTO(SQLModel):
    cnpj: int
    nome: str
    contato: str
    endereco: str
