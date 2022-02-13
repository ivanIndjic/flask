"""empty message

Revision ID: 59b153e36b3f
Revises: 158d20707cff
Create Date: 2022-02-11 20:50:47.534051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59b153e36b3f'
down_revision = '158d20707cff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###