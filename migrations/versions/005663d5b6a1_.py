"""empty message

Revision ID: 005663d5b6a1
Revises: 46222d4c823c
Create Date: 2023-09-09 18:13:18.969168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '005663d5b6a1'
down_revision = '46222d4c823c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('token')

    # ### end Alembic commands ###
