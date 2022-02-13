"""empty message

Revision ID: 77937f6f3896
Revises: f05459d20a78
Create Date: 2022-02-12 23:04:35.737554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77937f6f3896'
down_revision = 'f05459d20a78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('created_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('post', sa.Column('modified_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('post', sa.Column('blog', sa.Integer(), nullable=True))
    op.add_column('post', sa.Column('author', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'post', ['name'])
    op.drop_constraint('post_blog_id_fkey', 'post', type_='foreignkey')
    op.drop_constraint('post_author_id_fkey', 'post', type_='foreignkey')
    op.create_foreign_key(None, 'post', 'blog', ['blog'], ['id'])
    op.create_foreign_key(None, 'post', 'author', ['author'], ['id'])
    op.drop_column('post', 'author_id')
    op.drop_column('post', 'blog_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.create_foreign_key('post_author_id_fkey', 'post', 'author', ['author_id'], ['id'])
    op.create_foreign_key('post_blog_id_fkey', 'post', 'blog', ['blog_id'], ['id'])
    op.drop_constraint(None, 'post', type_='unique')
    op.drop_column('post', 'author')
    op.drop_column('post', 'blog')
    op.drop_column('post', 'modified_time')
    op.drop_column('post', 'created_time')
    # ### end Alembic commands ###
