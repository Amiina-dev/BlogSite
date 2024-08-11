"""add content column to post

Revision ID: eaa2008f9fc4
Revises: b5b899f517c2
Create Date: 2024-08-10 17:38:51.548928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaa2008f9fc4'
down_revision: Union[str, None] = 'b5b899f517c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
