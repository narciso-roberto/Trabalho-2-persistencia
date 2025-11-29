"""tirando tpo de transacao

Revision ID: 076cee00b057
Revises: 785fcf96dec9
Create Date: 2025-11-22 17:04:13.552133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '076cee00b057'
down_revision: Union[str, Sequence[str], None] = '785fcf96dec9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
