from sqlmodel import SQLModel

class PrdutoTransacaoFornecedorDTO(SQLModel):
    produto_id: int | None = None
    fornecedor_id: int | None = None
    quantidade: int | None = None
    
class CreateTransacaoDTO(SQLModel):
    itens: list[PrdutoTransacaoFornecedorDTO]