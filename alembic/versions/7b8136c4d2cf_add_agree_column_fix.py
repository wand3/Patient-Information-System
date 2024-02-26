"""add agree column fix

Revision ID: 7b8136c4d2cf
Revises: 678e14a9571d
Create Date: 2024-02-25 18:57:35.438312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b8136c4d2cf'
down_revision: Union[str, None] = '678e14a9571d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
