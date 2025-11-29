"""tirando tpo de transacao

Revision ID: a4752ceaeae5
Revises: 3b9e2564f710
Create Date: 2025-11-22 17:07:47.888492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'a4752ceaeae5'
down_revision: Union[str, Sequence[str], None] = '3b9e2564f710'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
