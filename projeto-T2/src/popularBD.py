from sqlmodel import SQLModel, Session, create_engine
from models.produto import Produto
from models.fornecedor import Fornecedor
from models.ProdutoTransacaoFornecedor import ProdutoTransacaoFornecedor
from models.transacao import Transacao
from database.database import engine

with Session(engine) as session:

    # # -----------------------
    # # 10 FORNECEDORES
    # # -----------------------
    # fornecedores = [
    #     Fornecedor(idForn=1, cnpj=11111111111111, nome="Fornecedor A", contato="contatoA@gmail.com", endereco="Rua A, 100"),
    #     Fornecedor(idForn=2, cnpj=22222222222222, nome="Fornecedor B", contato="contatoB@gmail.com", endereco="Rua B, 200"),
    #     Fornecedor(idForn=3, cnpj=33333333333333, nome="Fornecedor C", contato="contatoC@gmail.com", endereco="Rua C, 300"),
    #     Fornecedor(idForn=4, cnpj=44444444444444, nome="Fornecedor D", contato="contatoD@gmail.com", endereco="Rua D, 400"),
    #     Fornecedor(idForn=5, cnpj=55555555555555, nome="Fornecedor E", contato="contatoE@gmail.com", endereco="Rua E, 500"),
    #     Fornecedor(idForn=6, cnpj=66666666666666, nome="Fornecedor F", contato="contatoF@gmail.com", endereco="Rua F, 600"),
    #     Fornecedor(idForn=7, cnpj=77777777777777, nome="Fornecedor G", contato="contatoG@gmail.com", endereco="Rua G, 700"),
    #     Fornecedor(idForn=8, cnpj=88888888888888, nome="Fornecedor H", contato="contatoH@gmail.com", endereco="Rua H, 800"),
    #     Fornecedor(idForn=9, cnpj=99999999999999, nome="Fornecedor I", contato="contatoI@gmail.com", endereco="Rua I, 900"),
    #     Fornecedor(idForn=10, cnpj=10101010101010, nome="Fornecedor J", contato="contatoJ@gmail.com", endereco="Rua J, 1000"),
    # ]

    # session.add_all(fornecedores)

    # # -----------------------
    # # 10 PRODUTOS
    # # -----------------------
    # produtos = [
    #     Produto(idProd=1, mercadoria="Arroz", valor=20.50, quantidade=100, categoria="Alimento"),
    #     Produto(idProd=2, mercadoria="Feijão", valor=10.0, quantidade=150, categoria="Alimento"),
    #     Produto(idProd=3, mercadoria="Macarrão", valor=7.8, quantidade=200, categoria="Alimento"),
    #     Produto(idProd=4, mercadoria="Óleo", valor=6.5, quantidade=180, categoria="Alimento"),
    #     Produto(idProd=5, mercadoria="Açúcar", valor=5.2, quantidade=140, categoria="Alimento"),
    #     Produto(idProd=6, mercadoria="Sabonete", valor=2.5, quantidade=300, categoria="Higiene"),
    #     Produto(idProd=7, mercadoria="Detergente", valor=3.0, quantidade=250, categoria="Limpeza"),
    #     Produto(idProd=8, mercadoria="Shampoo", valor=12.0, quantidade=120, categoria="Higiene"),
    #     Produto(idProd=9, mercadoria="Café", valor=15.0, quantidade=90, categoria="Alimento"),
    #     Produto(idProd=10, mercadoria="Sal", valor=2.0, quantidade=500, categoria="Alimento"),
    # ]

    # session.add_all(produtos)



    # # -----------------------
    # # TRANSACOES
    # # -----------------------
    # transacoes = [
    #     Transacao(quantidade=50, data_transacao="2025-01-01"),
    #     Transacao(quantidade=70, data_transacao="2025-01-02"),
    #     Transacao(quantidade=20, data_transacao="2025-01-03"),
    #     Transacao(quantidade=40, data_transacao="2025-01-04"),
    #     Transacao(quantidade=10, data_transacao="2025-01-05"),
    #     Transacao(quantidade=100, data_transacao="2025-01-06"),
    #     Transacao(quantidade=60, data_transacao="2025-01-07"),
    #     Transacao(quantidade=30, data_transacao="2025-01-08"),
    #     Transacao(quantidade=80, data_transacao="2025-01-09"),
    #     Transacao(quantidade=25, data_transacao="2025-01-10"),
    # ]

    # session.add_all(transacoes)

    # # -----------------------
    # # ProdutoTransacaoFornecedor
    # # -----------------------

    ptf = [
        ProdutoTransacaoFornecedor(produto_id=1, fornecedor_id=4, transacao_id=1),
        ProdutoTransacaoFornecedor(produto_id=1, fornecedor_id=5, transacao_id=1),
    ]

    session.add_all(ptf)

    # SALVA TUDO
    session.commit()

print("Banco populado com sucesso!")
