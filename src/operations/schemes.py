from pydantic import BaseModel


class OperationCreate(BaseModel):
    ip: str
    status: str
    event: str
