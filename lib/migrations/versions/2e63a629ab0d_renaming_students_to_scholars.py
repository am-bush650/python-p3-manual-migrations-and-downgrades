"""Renaming students to scholars

Revision ID: 2e63a629ab0d
Revises: 791279dd0760
Create Date: 2025-03-12 21:39:18.556056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e63a629ab0d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    
