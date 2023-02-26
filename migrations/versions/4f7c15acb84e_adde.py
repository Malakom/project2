"""adde

Revision ID: 4f7c15acb84e
Revises: cbbb9828cf82
Create Date: 2023-01-30 11:37:59.612723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f7c15acb84e'
down_revision = 'cbbb9828cf82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('country_currency', sa.String(), nullable=False))
        batch_op.drop_column('description')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('countries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('country_currency')

    # ### end Alembic commands ###
