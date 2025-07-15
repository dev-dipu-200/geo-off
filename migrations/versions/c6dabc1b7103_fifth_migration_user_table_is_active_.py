"""fifth migration user table is_active make boolean

Revision ID: c6dabc1b7103
Revises: e9d5823624bc
Create Date: 2025-07-15 16:10:27.608998
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c6dabc1b7103'
down_revision: Union[str, Sequence[str], None] = 'e9d5823624bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Step 1: Normalize any non-boolean, string-like values to valid integers
    op.execute("""
        UPDATE users
        SET is_active = CASE
            WHEN is_active::text IN ('true', '1', 'yes', 'active', 'TRUE', 't') THEN 1
            ELSE 0
        END;
    """)

    # Step 2: Alter column type from INTEGER to BOOLEAN using a safe cast
    op.execute("""
        ALTER TABLE users
        ALTER COLUMN is_active TYPE BOOLEAN
        USING is_active::boolean;
    """)


def downgrade() -> None:
    """Downgrade schema."""

    # Revert the column back to INTEGER (true → 1, false → 0)
    op.execute("""
        ALTER TABLE users
        ALTER COLUMN is_active TYPE INTEGER
        USING CASE
            WHEN is_active = TRUE THEN 1
            ELSE 0
        END;
    """)
