"""adiconar valor para a tabela produto_transacao_fornecedor

Revision ID: 21a9b4c49dce
Revises: 06651807b851
Create Date: 2025-11-30 22:19:14.137313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '21a9b4c49dce'
down_revision: Union[str, Sequence[str], None] = '06651807b851'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('produto_transacao_fornecedor', sa.Column('valor', sa.Float(), nullable=False))

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('produto_transacao_fornecedor', 'valor')
