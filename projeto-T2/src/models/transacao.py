from sqlmodel import Field, SQLModel

class Transacao(SQLModel, table=True):
    produto_id: int = Field(foreign_key="produto.idProd", primary_key=True)
    fornecedor_id: int = Field(foreign_key="fornecedor.idForn", primary_key=True)
    tipo: str
    quantidade: int # 0 - saída | 1 - entrada
    data_transacao: str | None = Field(default=None)