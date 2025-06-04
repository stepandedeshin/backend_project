"""empty message

Revision ID: 90e6ab14e78c
Revises: 
Create Date: 2025-05-20 15:01:40.386152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90e6ab14e78c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('login', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
