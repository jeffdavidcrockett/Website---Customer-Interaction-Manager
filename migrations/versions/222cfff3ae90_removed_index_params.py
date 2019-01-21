"""removed index params

Revision ID: 222cfff3ae90
Revises: 13ba4f9fa9a5
Create Date: 2019-01-21 01:35:56.806471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '222cfff3ae90'
down_revision = '13ba4f9fa9a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_interaction_client_id', table_name='interaction')
    op.drop_index('ix_interaction_type_of', table_name='interaction')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_interaction_type_of', 'interaction', ['type_of'], unique=False)
    op.create_index('ix_interaction_client_id', 'interaction', ['client_id'], unique=False)
    # ### end Alembic commands ###
