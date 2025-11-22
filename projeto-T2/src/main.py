# from sqlmodel import SQLModel, create_engine, Session


# from models.fornecedor import Fornecedor
# from models.produto import Produto
# from models.produto import ProdutoFornecedor
# from models.transacao import Transacao

# produto_1 = Produto(
#     mercadoria="Café Torrado",
#     valor=18.50,
#     quantidade=30,
#     categoria="Alimentos"
# )

# produto_2 = Produto(
#     mercadoria="Monitor 24 Polegadas",
#     valor=799.90,
#     quantidade=10,
#     categoria="Eletrônicos"
# )

# fornecedor_1 = Fornecedor(
#     cnpj=12345678000199,
#     nome="Café Bom Ltda",
#     contato="(85) 99999-1111",
#     endereco="Rua das Flores, 123"
# )

# fornecedor_2 = Fornecedor(
#     cnpj=98765432000188,
#     nome="Tech Distribuidora SA",
#     contato="(11) 98888-2222",
#     endereco="Avenida Central, 456"
# )

# pf_1 = ProdutoFornecedor(
#     produto=1,
#     fornecedor=1
# )

# pf_2 = ProdutoFornecedor(
#     produto=2,
#     fornecedor=2
# )

# transacao_1 = Transacao(
#     produto_id=1,
#     fornecedor_id=1,
#     tipo=1,  # entrada
#     quantidade=20,
#     data_transacao="2025-11-17",
# )

# transacao_2 = Transacao(
#     produto_id=2,
#     fornecedor_id=2,
#     tipo=2,  # saída
#     quantidade=5,
#     data_transacao="2025-11-17",
# )

# engine = create_engine("sqlite:///database.db")

# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(produto_1)
#     session.add(fornecedor_1)
#     session.add(pf_1)
#     session.add(transacao_1)
#     session.commit()

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Esse trambolho de codigo faz com que o fastAPI veja a pasta PROJETO-T2 como a pasta raiz

from fastapi import FastAPI
from src.routers.produto_router import routerProduto




app = FastAPI(title="Sistema de Estoque")

app.include_router(routerProduto)



