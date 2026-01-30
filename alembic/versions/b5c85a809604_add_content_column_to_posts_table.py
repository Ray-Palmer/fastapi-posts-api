"""add content column to posts table

Revision ID: b5c85a809604
Revises: 279b7286b58a
Create Date: 2026-01-30 11:35:37.169592

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b5c85a809604"
down_revision: Union[str, Sequence[str], None] = "279b7286b58a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
