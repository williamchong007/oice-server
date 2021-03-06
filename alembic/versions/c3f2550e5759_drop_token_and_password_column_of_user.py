"""Drop token and password column of user

Revision ID: c3f2550e5759
Revises: 8bfb33053381
Create Date: 2017-06-07 04:07:41.800671

"""

# revision identifiers, used by Alembic.
revision = 'c3f2550e5759'
down_revision = '8bfb33053381'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=1024), nullable=True))
    op.add_column('user', sa.Column('password', sa.VARBINARY(length=1137), nullable=True))
    # ### end Alembic commands ###
