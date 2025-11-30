from sqlmodel import Field, SQLModel, Relationship
from models.transacao import Transacao 

class ProdutoTransacaoFornecedor(SQLModel, table=True):
    produto_id: int = Field(foreign_key="produto.idProd", primary_key=True)
    fornecedor_id: int = Field(foreign_key="fornecedor.idForn", primary_key=True)
    transacao_id: int = Field(foreign_key="transacao.transacao_id", primary_key=True)

    produto: "Produto" = Relationship(back_populates="transacoesProduto")
    fornecedor: "Fornecedor" = Relationship(back_populates="transacoesFornecedor")
    transacao: "Transacao" = Relationship(back_populates="itens")
    


from models.fornecedor import Fornecedor
from models.transacao import TransacaoResponse


class PTFResponse(SQLModel):
    model_config = {"from_attributes": True}
    produto: "Produto" = Relationship(back_populates="transacoesProduto")
    fornecedor: Fornecedor 
    transacao: TransacaoResponse


ProdutoTransacaoFornecedor.model_rebuild()
