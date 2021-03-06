"""Fix PROD DB out-sync

Revision ID: 30a75d1e735
Revises: 4d5807cb5f7
Create Date: 2016-11-21 10:18:01.271930

"""

# revision identifiers, used by Alembic.
revision = '30a75d1e735'
down_revision = '3d2e1021492'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('attribute_ibfk_3', table_name='attribute', type_="foreignkey")
    op.alter_column('attribute', 'block_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.create_foreign_key('attribute_ibfk_3', 'attribute', 'block', ['block_id'], ['id'])
    op.alter_column('attribute_definition', 'required',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False, server_default=sa.text("'0'"))
    op.create_index('ks_position_idx', 'block', ['ks_id', 'position'], unique=False)
    op.drop_index('block_id', table_name='block')
    op.drop_index('block_position_idx', table_name='block')
    op.alter_column('character', 'config',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column('ks', 'is_deleted',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False, server_default=sa.text("'0'"))
    op.alter_column('macro', 'is_hidden',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    op.alter_column('option', 'count',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    op.alter_column('project', 'is_default_lib_project',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    op.alter_column('project', 'is_deleted',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    op.alter_column('project', 'is_lib_project',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', 'is_lib_project',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'0'"))
    op.alter_column('project', 'is_deleted',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'0'"))
    op.alter_column('project', 'is_default_lib_project',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'0'"))
    op.alter_column('option', 'count',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               existing_server_default=sa.text("'0'"))
    op.alter_column('macro', 'is_hidden',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'0'"))
    op.alter_column('character', 'config',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.create_index('block_position_idx', 'block', ['position'], unique=False)
    op.create_index('block_id', 'block', ['id'], unique=False)
    op.drop_index('ks_position_idx', table_name='block')
    op.alter_column('attribute_definition', 'required',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('attribute', 'block_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    ### end Alembic commands ###
