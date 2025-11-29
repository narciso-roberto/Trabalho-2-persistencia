from fastapi import FastAPI
from routers.produto_router import routerProduto
from routers.fornecedor_router import routerFornecedor

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

app.include_router(routerProduto)
app.include_router(routerFornecedor)