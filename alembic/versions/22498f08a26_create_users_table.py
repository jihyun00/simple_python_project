"""create users table

Revision ID: 22498f08a26
Revises: 
Create Date: 2015-03-10 01:29:36.978605

"""

# revision identifiers, used by Alembic.
revision = '22498f08a26'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('key', sa.String(20), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')