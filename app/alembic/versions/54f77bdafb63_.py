"""empty message

Revision ID: 54f77bdafb63
Revises: 238762ab5bcd
Create Date: 2023-12-08 15:05:24.398272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54f77bdafb63'
down_revision: Union[str, None] = '238762ab5bcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('friends', sa.Column('email', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('friends', 'email')
    # ### end Alembic commands ###
