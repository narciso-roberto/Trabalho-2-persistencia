"""tirando tpo de transacao

Revision ID: 3b9e2564f710
Revises: de50405c8106
Create Date: 2025-11-22 17:06:04.582393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '3b9e2564f710'
down_revision: Union[str, Sequence[str], None] = 'de50405c8106'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
