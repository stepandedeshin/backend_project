"""empty message

Revision ID: f539b0988b63
Revises: 90e6ab14e78c
Create Date: 2025-06-02 23:59:18.839763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f539b0988b63'
down_revision: Union[str, None] = '90e6ab14e78c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
