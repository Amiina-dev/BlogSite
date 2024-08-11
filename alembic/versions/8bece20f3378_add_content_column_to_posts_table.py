"""add content column to posts table

Revision ID: 8bece20f3378
Revises: 0bd4eef994bf
Create Date: 2024-08-11 03:59:29.287706

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8bece20f3378"
down_revision: Union[str, None] = "0bd4eef994bf"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
