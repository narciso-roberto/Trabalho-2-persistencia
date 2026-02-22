# 📦 Sistema de Controle de Estoque

API RESTful desenvolvida com **FastAPI** e banco de dados assíncrono, focada em modelagem relacional eficiente e consultas performáticas em cenários reais de gestão de estoque.

---

## 🚀 Objetivo do Projeto

Este projeto foi desenvolvido durante a graduação com foco em:

- Uso eficiente de SQL  
- Modelagem relacional consistente  
- Consultas performáticas com `JOIN`  
- Uso adequado de *eager loading*  
- Prevenção do problema **N+1**  
- Estruturação de API REST escalável  
- Controle de versionamento com Git e GitHub  

---

## 🛠️ Tecnologias Utilizadas

- **FastAPI** — Framework web moderno e performático  
- **SQLModel** — ORM baseado em SQLAlchemy + Pydantic  
- **SQLAlchemy (Async)**  
- **Alembic** — Controle de migrações  
- Banco de dados assíncrono  
- **Python 3.10+**  
- **Git & GitHub** — Versionamento e fluxo de desenvolvimento  

---

## 📚 Funcionalidades

- Cadastro de produtos  
- Registro de entradas de estoque  
- Registro de saídas de estoque  
- Controle de saldo atualizado automaticamente  
- Relacionamentos entre entidades  
- Consultas otimizadas com `JOIN`  
- Carregamento eficiente de dados relacionados (*eager loading*)  

---

## 🧠 Conceitos Aplicados

- Modelagem relacional normalizada  
- Relacionamentos One-to-Many  
- Prevenção de **N+1 queries**  
- Uso estratégico de índices  
- Separação de camadas (`models`, `schemas`, `services`, `routers`)  
- Migrations versionadas com Alembic  
- Controle de branches e commits estruturados  
