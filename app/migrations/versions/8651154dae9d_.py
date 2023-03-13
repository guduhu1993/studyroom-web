"""empty message

Revision ID: 8651154dae9d
Revises: 
Create Date: 2022-03-10 14:27:59.996990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8651154dae9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('user_type', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('message_code',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('code', sa.String(length=6), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message_code')
    op.drop_table('user')
    # ### end Alembic commands ###
