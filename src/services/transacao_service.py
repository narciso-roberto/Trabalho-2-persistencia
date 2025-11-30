from database.database import engine
from sqlmodel import Session, select
from sqlalchemy.orm import joinedload

from models.transacao import Transacao
from models.ProdutoTransacaoFornecedor import ProdutoTransacaoFornecedor
from models.produto import Produto

from dtos.transacaoRespostaDTO import TransacaoRespostaDTO, TransacaoProdutoRespostaDTO, TransacaoFornecedorRespostaDTO
from dtos.pagination import Pagination
from dtos.createTransacaoDTO import CreateTransacaoDTO
from dtos.updateTransacaoDTO import UpdateTransacaoDTO

from datetime import datetime

import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

def resgatarTodas(offset: int, limit: int, data_incial: datetime | None, data_final: datetime | None) -> Pagination[TransacaoRespostaDTO] | str:
    if data_incial and data_final and data_incial > data_final:
        return "Data inicial não pode ser maior que a data final."
    
    with Session(engine) as session:
        try:
            statement = select(Transacao)
            if data_incial and data_final:
                statement = statement.where(Transacao.data_transacao.between(data_incial, data_final))    
            
            statement = statement.offset(offset).limit(limit).options(joinedload(Transacao.itens))
            resultados = session.exec(statement).unique()
            listaTransacoes = resultados.all()
            
            count = len(listaTransacoes)
            
            resp = Pagination()
            resp.__populate__(offset//limit + 1, limit, count)
            
            for t in listaTransacoes:
                transacao = TransacaoRespostaDTO()
                transacao.transacao_id = t.transacao_id
                transacao.quantidade = t.quantidade  
                transacao.data_transacao = t.data_transacao
                
                for item in t.itens:
                    transacao.produtos.append(TransacaoProdutoRespostaDTO(
                        produto_id=item.produto.idProd,
                        mercadoria=item.produto.mercadoria,
                        quantidade=item.produto.quantidade,
                        categoria=item.produto.categoria
                    ))
                    
                    transacao.fornecedores.append(TransacaoFornecedorRespostaDTO(
                        fornecedor_id=item.fornecedor.idForn,
                        nome=item.fornecedor.nome,
                        cnpj=item.fornecedor.cnpj
                    ))
                    
                resp.content.append(transacao)  
                              
            return resp
                                
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")
        
def resgatarUm(id: int) -> TransacaoRespostaDTO | str:
    with Session(engine) as session:
        try:
            transacao = session.get(Transacao, id)
            
            if not transacao:
                return "Transacao não encontrada."
            
            resp = TransacaoRespostaDTO()
            resp.transacao_id = transacao.transacao_id
            resp.quantidade = transacao.quantidade
            resp.data_transacao = transacao.data_transacao
            
            for item in transacao.itens:
                resp.produtos.append(TransacaoProdutoRespostaDTO(
                    produto_id=item.produto.idProd,
                    mercadoria=item.produto.mercadoria,
                    quantidade=item.produto.quantidade,
                    categoria=item.produto.categoria
                ))
                
                resp.fornecedores.append(TransacaoFornecedorRespostaDTO(
                    fornecedor_id=item.fornecedor.idForn,
                    nome=item.fornecedor.nome,
                    cnpj=item.fornecedor.cnpj
                ))
                
            return resp
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")
        
def criar(transacao: CreateTransacaoDTO) -> str:
    with Session(engine) as session:
        try:
            nova_transacao = Transacao()
            nova_transacao.quantidade = sum(item.quantidade for item in transacao.itens if item.quantidade)
            nova_transacao.data_transacao = datetime.now()
            
            session.add(nova_transacao)
            session.flush()
            
            for item in transacao.itens:
                p_t_f = ProdutoTransacaoFornecedor(
                    produto_id=item.produto_id,
                    fornecedor_id=item.fornecedor_id,
                    transacao_id=nova_transacao.transacao_id,
                    quantidade=item.quantidade,
                )
                
                session.get(Produto, item.produto_id).quantidade += item.quantidade
                session.flush()
                
                session.add(p_t_f)
                
            session.commit()
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")
        
def atualizar(id: int, transacao: UpdateTransacaoDTO) -> str:
    with Session(engine) as session:
        try:
            transacao_existente = session.get(Transacao, id)

            if not transacao_existente:
                return "Transacao não encontrada."
            
            if len(transacao.itens) > 0:
                transacao_existente.quantidade = sum(item.quantidade for item in transacao.itens if item.quantidade)    
                
                session.query(ProdutoTransacaoFornecedor).filter(
                    ProdutoTransacaoFornecedor.transacao_id == transacao_existente.transacao_id
                ).delete()
                session.flush()
                
                for item in transacao.itens:
                    p_t_f = ProdutoTransacaoFornecedor(
                        produto_id=item.produto_id,
                        fornecedor_id=item.fornecedor_id,
                        transacao_id=id,
                        quantidade=item.quantidade,
                    )
                    
                    session.get(Produto, item.produto_id).quantidade += item.quantidade
                    session.flush()
                    
                    session.add(p_t_f)
                
            if transacao.data_transacao:
                transacao_existente.data_transacao = transacao.data_transacao
            
            session.add(transacao_existente)
            session.commit()
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")
        
def deletar(id: int) -> str:
    with Session(engine) as session:
        try:
            transacao_existente = session.get(Transacao, id)
            
            if not transacao_existente:
                return "Transacao não encontrada."
            
            session.delete(transacao_existente)
            session.commit()
        except Exception as e:
            session.rollback()
            return(f"Error: {e}")