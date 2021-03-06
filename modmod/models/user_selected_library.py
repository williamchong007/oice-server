import sqlalchemy as sa

from modmod.models.base import (
    Base,
)

user_selected_library = sa.Table(
    'user_selected_library',
    Base.metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
    sa.Column('library_id', sa.Integer, sa.ForeignKey('library.id'), nullable=False),
    sa.UniqueConstraint('user_id', 'library_id', name='user_id_library_id')
)
