"""empty message

Revision ID: e454b1597ab0
Revises: 
Create Date: 2021-01-19 11:50:17.899068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e454b1597ab0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'author', ['name'])
    op.create_foreign_key(None, 'book_author_link', 'author', ['foreign_b'], ['id'])
    op.create_foreign_key(None, 'book_author_link', 'book', ['foreign_a'], ['id'])
    op.create_foreign_key(None, 'book_subject_link', 'subject', ['foreign_b'], ['id'])
    op.create_foreign_key(None, 'book_subject_link', 'book', ['foreign_a'], ['id'])
    op.create_foreign_key(None, 'printing', 'website', ['website'], ['id'])
    op.create_foreign_key(None, 'printing', 'book', ['book_id'], ['id'])
    op.drop_column('subject', 'count')
    op.drop_index('ix_website_url_id', table_name='website_url')
    op.create_foreign_key(None, 'website_url', 'website', ['site_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'website_url', type_='foreignkey')
    op.create_index('ix_website_url_id', 'website_url', ['id'], unique=False)
    op.add_column('subject', sa.Column('count', sa.BIGINT(), nullable=True))
    op.drop_constraint(None, 'printing', type_='foreignkey')
    op.drop_constraint(None, 'printing', type_='foreignkey')
    op.drop_constraint(None, 'book_subject_link', type_='foreignkey')
    op.drop_constraint(None, 'book_subject_link', type_='foreignkey')
    op.drop_constraint(None, 'book_author_link', type_='foreignkey')
    op.drop_constraint(None, 'book_author_link', type_='foreignkey')
    op.drop_constraint(None, 'author', type_='unique')
    # ### end Alembic commands ###
