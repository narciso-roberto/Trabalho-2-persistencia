from sqlmodel import Field, SQLModel, Relationship


class Transacao(SQLModel, table=True):
    transacao_id: int | None = Field(default=None, primary_key=True)
    quantidade: int 
    data_transacao: str | None = Field(default=None)

    itens: list["ProdutoTransacaoFornecedor"] = Relationship(back_populates="transacao")



class TransacaoResponse(SQLModel):
    model_config = {"from_attributes": True}
    quantidade: int 
    data_transacao: str | None 
    

Transacao.model_rebuild()
