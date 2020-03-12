import datetime
import sqlalchemy as sa
from pypi_org.data.modelbase import SqlAlchemyBase


class Audit(SqlAlchemyBase):
    __tablename__ = 'auditing'

    id: str = sa.Column(sa.String, primary_key=True)
    created_date: datetime.datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    description: str = sa.Column(sa.String)
