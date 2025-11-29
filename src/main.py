from fastapi import FastAPI
from routers.produto_router import routerProduto
from routers.fornecedor_router import routerFornecedor
from database.database import create_db_and_tables

tags_metadata = [
    {
        "name": "Fornecedor",
        "description": "Operações de gerenciamento de fornecedores",
    },
    {
        "name": "Produto",
        "description": "Operações de gerenciamento de produtos",
    },
]

app = FastAPI(
    title="Sistema de Estoque",
    openapi_tags=tags_metadata,
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(routerProduto)
app.include_router(routerFornecedor)