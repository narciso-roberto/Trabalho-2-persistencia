from sqlmodel import SQLModel

class TransacaoFornecedorRespostaDTO(SQLModel):
    fornecedor_id: int | None = None
    nome: str | None = None
    cnpj: int | None = None

class TransacaoProdutoRespostaDTO(SQLModel):
    produto_id: int | None = None
    mercadoria: str | None = None
    quantidade: int | None = None
    categoria: str | None = None
    
class TransacaoRespostaDTO(SQLModel):
    transacao_id: int | None = None
    quantidade: int | None = None
    data_transacao: str | None = None
    
    produtos: list[TransacaoProdutoRespostaDTO]= []
    fornecedores: list[TransacaoFornecedorRespostaDTO] = []