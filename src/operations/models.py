from sqlalchemy import Table, Column, String, MetaData

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("ip", String, primary_key=True),
    Column("status", String),
    Column("event", String),
)