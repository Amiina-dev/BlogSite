"""auto vote

Revision ID: 1e46d00021e5
Revises: 8e5654e84778
Create Date: 2024-08-11 04:04:38.488530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e46d00021e5'
down_revision: Union[str, None] = '8e5654e84778'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
