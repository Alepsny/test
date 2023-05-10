from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON


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





