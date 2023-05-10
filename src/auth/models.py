from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData

from ..database import Base

metadata = MetaData()

data = Table(
    "roles",
    metadata,
    Column("ip", String, primary_key= True),
    Column("status", String, nullable=False),
    Column("event", String)
)

users = Table(
    "users",
    metadata,
    Column("ip", String, primary_key=True),
    Column("status", String, nullable=False),
    Column("event", String, nullable=False),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    ip = Column(String, primary_key=True)
    status = Column(String, nullable=False)
    event = Column(String, nullable=False)
