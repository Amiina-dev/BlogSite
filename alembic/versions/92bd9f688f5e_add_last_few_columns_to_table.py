"""add last few columns to table

Revision ID: 92bd9f688f5e
Revises: 9537d07d177f
Create Date: 2024-08-11 04:12:49.485395

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "92bd9f688f5e"
down_revision: Union[str, None] = "9537d07d177f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
