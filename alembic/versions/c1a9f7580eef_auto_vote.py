"""auto vote

Revision ID: c1a9f7580eef
Revises: 92bd9f688f5e
Create Date: 2024-08-11 04:18:47.535533

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1a9f7580eef'
down_revision: Union[str, None] = '92bd9f688f5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
