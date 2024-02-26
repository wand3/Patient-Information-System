"""add agree column

Revision ID: 678e14a9571d
Revises: d5e2ffeec256
Create Date: 2024-02-25 18:55:53.803805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '678e14a9571d'
down_revision: Union[str, None] = 'd5e2ffeec256'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
