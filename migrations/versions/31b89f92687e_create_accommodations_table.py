"""create accommodations table

Revision ID: 31b89f92687e
Revises: f85e4333b1b6
Create Date: 2019-06-07 18:47:05.757944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31b89f92687e'
down_revision = 'f85e4333b1b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accommodation',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('host_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=120), nullable=True),
        sa.Column('num_guests', sa.Integer(), nullable=False),
        sa.Column('num_bedrooms', sa.Integer(), nullable=False),
        sa.Column('num_beds', sa.Integer(), nullable=False),
        sa.Column('num_bathrooms', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('suburb', sa.String(length=32), nullable=True),
        sa.Column('city', sa.String(length=32), nullable=False),
        sa.Column('state', sa.String(length=32), nullable=True),
        sa.Column('country', sa.String(length=32), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('property_type', sa.String(length=32), nullable=False),
        sa.Column('amenities', sa.Text(), nullable=True),
        sa.Column('rating', sa.Float(), nullable=True),
        sa.Column('num_reviews', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['host_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accommodation')
    # ### end Alembic commands ###
