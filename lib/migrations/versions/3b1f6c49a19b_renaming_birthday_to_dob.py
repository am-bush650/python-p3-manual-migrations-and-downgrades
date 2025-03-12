"""Renaming birthday to dob

Revision ID: 3b1f6c49a19b
Revises: 2e63a629ab0d
Create Date: 2025-03-12 21:52:12.117750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b1f6c49a19b'
down_revision = '2e63a629ab0d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('scholars', 'birthday', new_column_name='dob')


def downgrade() -> None:
    op.alter_column('scholars', 'dob', new_column_name='birthday')