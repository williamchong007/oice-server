"""Add unique constraint on asset_user

Revision ID: 971e429b53d0
Revises: 6fb55a4132fe
Create Date: 2017-04-06 10:05:49.136606

"""

# revision identifiers, used by Alembic.
revision = '971e429b53d0'
down_revision = '6fb55a4132fe'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('asset_id_asset_type_id', 'asset_asset_types', ['asset_id', 'asset_type_id'])
    op.create_unique_constraint('asset_id_user_id', 'asset_user', ['asset_id', 'user_id'])
    op.create_unique_constraint('character_id_asset_id', 'character_fgimages', ['character_id', 'asset_id'])
    op.create_unique_constraint('story_id_library_id', 'story_library', ['story_id', 'library_id'])
    op.create_unique_constraint('user_id_library_id', 'user_library', ['user_id', 'library_id'])
    op.create_unique_constraint('user_id_story_id', 'user_story', ['user_id', 'story_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('asset_id_asset_type_id', 'asset_asset_types', type_='unique')
    op.drop_constraint('asset_id_user_id', 'asset_user', type_='unique')
    op.drop_constraint('character_id_asset_id', 'character_fgimages', type_='unique')
    op.drop_constraint('story_id_library_id', 'story_library', type_='unique')
    op.drop_constraint('user_id_library_id', 'user_library', type_='unique')
    op.drop_constraint('user_id_story_id', 'user_story', type_='unique')
    # ### end Alembic commands ###