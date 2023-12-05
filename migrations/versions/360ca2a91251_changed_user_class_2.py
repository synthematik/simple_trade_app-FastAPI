"""Changed User class #2

Revision ID: 360ca2a91251
Revises: ac673657afce
Create Date: 2023-12-04 18:45:04.159326

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '360ca2a91251'
down_revision: Union[str, None] = 'ac673657afce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('role', 'permissions',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('user', 'password',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(),
               type_=postgresql.JSON(astext_type=sa.Text()),
               existing_nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.String(),
               type_=postgresql.JSON(astext_type=sa.Text()),
               existing_nullable=False)
    op.alter_column('role', 'permissions',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    # ### end Alembic commands ###