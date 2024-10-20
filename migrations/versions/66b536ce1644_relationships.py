"""Relationships

Revision ID: 66b536ce1644
Revises: 7c0add1879b5
Create Date: 2024-10-20 11:58:38.856766

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '66b536ce1644'
down_revision = '7c0add1879b5'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        # Temporarily add group_id as nullable
        batch_op.add_column(sa.Column('group_id', sa.Integer(), nullable=True))
        batch_op.alter_column('question',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=500),
               existing_nullable=False)
        batch_op.alter_column('answer',
               existing_type=sa.TEXT(),
               type_=sa.String(length=500),
               existing_nullable=False)
        # Create the foreign key constraint
        batch_op.create_foreign_key('fk_flashcard_group', 'group', ['group_id'], ['id'])

    # Now that the column is added, make it NOT NULL
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        batch_op.alter_column('group_id',
               existing_type=sa.Integer(),
               nullable=False)

    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        # Drop the foreign key constraint by name
        batch_op.drop_constraint('fk_flashcard_group', type_='foreignkey')
        batch_op.alter_column('answer',
               existing_type=sa.String(length=500),
               type_=sa.TEXT(),
               existing_nullable=False)
        batch_op.alter_column('question',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)
        batch_op.drop_column('group_id')

    # ### end Alembic commands ###