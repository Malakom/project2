"""added

Revision ID: c3d8c3fc03a3
Revises: d73dfb68160c
Create Date: 2023-01-27 17:38:04.601963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3d8c3fc03a3'
down_revision = 'd73dfb68160c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(None, ['rating'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('rating')

    # ### end Alembic commands ###
