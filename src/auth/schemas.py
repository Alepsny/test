from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    ip: str
    status: str
    event: str


    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    ip: str
    status: str
    event: str
