
class Fornecedor(SQLModel, table=True):
    cnpj: int
    nome: str
    contato: str
    endereco: str
