from sqlmodel import Field, SQLModel, Relationship

class ProdutoTransacaoFornecedor(SQLModel, table=True):
    produto_id: int = Field(foreign_key="produto.idProd", primary_key=True)
    fornecedor_id: int = Field(foreign_key="fornecedor.idForn", primary_key=True)
    transacao_id: int = Field(foreign_key="transacao.transacao_id", primary_key=True)


    fornecedor: "Fornecedor" = Relationship(back_populates="transacoes")



ProdutoTransacaoFornecedor.model_rebuild()
