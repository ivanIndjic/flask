"""empty message

Revision ID: 158d20707cff
Revises: 498c0554bf32
Create Date: 2022-02-11 20:46:15.870276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '158d20707cff'
down_revision = '498c0554bf32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('name', sa.String(length=200), nullable=True))
    op.create_unique_constraint(None, 'blog', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog', type_='unique')
    op.drop_column('blog', 'name')
    # ### end Alembic commands ###