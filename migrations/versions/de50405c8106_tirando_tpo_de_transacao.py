"""tirando tpo de transacao

Revision ID: de50405c8106
Revises: 076cee00b057
Create Date: 2025-11-22 17:04:41.234593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'de50405c8106'
down_revision: Union[str, Sequence[str], None] = '076cee00b057'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
