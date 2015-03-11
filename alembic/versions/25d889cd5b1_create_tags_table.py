"""create tags table

Revision ID: 25d889cd5b1
Revises: 22498f08a26
Create Date: 2015-03-10 01:29:41.304018

"""

# revision identifiers, used by Alembic.
revision = '25d889cd5b1'
down_revision = '22498f08a26'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'tags',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('tag', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('username', sa.String, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('tags')