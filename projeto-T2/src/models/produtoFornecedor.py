from sqlmodel import Field, SQLModel


class ProdutoFornecedor(SQLModel, table=True):
    produto: int = Field(foreign_key="produto.idProd", primary_key=True)
    fornecedor: int = Field(foreign_key="fornecedor.idForn", primary_key=True)