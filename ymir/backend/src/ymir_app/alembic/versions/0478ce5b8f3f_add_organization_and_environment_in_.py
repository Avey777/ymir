"""add organization and environment in user tbl

Revision ID: 0478ce5b8f3f
Revises: 501414124392
Create Date: 2022-06-27 10:48:30.195372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0478ce5b8f3f"
down_revision = "501414124392"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("organization", sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column("scene", sa.String(length=500), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_column("scene")
        batch_op.drop_column("organization")

    # ### end Alembic commands ###