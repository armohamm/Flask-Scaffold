"""empty message

Revision ID: 65f25e38f0be
Revises: b57c5c750dba
Create Date: 2018-11-03 18:52:42.080985

"""

# revision identifiers, used by Alembic.
revision = '65f25e38f0be'
down_revision = 'b57c5c750dba'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updateddate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('updateddate', sa.DATE(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###