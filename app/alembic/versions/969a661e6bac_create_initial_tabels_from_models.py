"""create initial tables from models

Revision ID: 969a661e6bac
Revises: 
Create Date: 2023-11-17 03:04:59.458643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '969a661e6bac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token_type', sa.String(), nullable=True),
    sa.Column('access_token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tokens_id'), 'tokens', ['id'], unique=False)

    # EDIT HERE UNTIL USERS TABLE COMPLETE
    # changed table name below from given "users" to "Users"
    op.create_table('Users',
    # index below complete
    sa.Column('id', sa.Integer(), nullable=False, index=True), 
    sa.Column('username', sa.String(), nullable=False, index=True),
    sa.Column('email', sa.String(), nullable=False, unique=True, index=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True, default=True),
    # don't think I need the superuser type on the line below
    # sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # CHECKLIST for crossing off indices for columns
    # [x] id column
    # [x] username column
    # [x] email column

    # [ ] CONCERN , posted in slack - double declarations of uniqueness or nullables between column
    # creation and indices above and below?
    op.create_index(op.f('ix_Users_id'), 'Users', ['id'], unique=False)
    op.create_index(op.f('ix_Users_username'), 'Users', ['username'], unique=True)
    op.create_index(op.f('ix_Users_email'), 'Users', ['email'], unique=True)
  



    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_full_name'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tokens_id'), table_name='tokens')
    op.drop_table('tokens')
    # ### end Alembic commands ###