"""test reverse

Revision ID: 5a9b60f37dbe
Revises: 58f326f5dd59
Create Date: 2023-09-30 16:45:00.470848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a9b60f37dbe'
down_revision = '58f326f5dd59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('strength', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.drop_column('strength')

    # ### end Alembic commands ###
