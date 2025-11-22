"""tirando tpo de transacao

Revision ID: 785fcf96dec9
Revises: bd15612f9691
Create Date: 2025-11-22 17:03:48.093519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '785fcf96dec9'
down_revision: Union[str, Sequence[str], None] = 'bd15612f9691'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
