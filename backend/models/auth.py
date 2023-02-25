from pydantic import BaseModel, Field


class AuthData(BaseModel):
    login: str = Field(..., min_length=4)
    password: str = Field(..., min_length=9)


class UserInfo(BaseModel):
    id: str = Field(...)
    login: str = Field(..., min_length=4)
    avatar: str = Field(...)
    description: str = Field(...)
