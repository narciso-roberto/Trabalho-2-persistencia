from sqlmodel import Field, SQLModel

class Transacao(SQLModel, table=True):
    transacao_id: int | None = Field(default=None, primary_key=True)
    tipo: str
    quantidade: int # 0 - saída | 1 - entrada
    data_transacao: str | None = Field(default=None)

Transacao.model_rebuild()
