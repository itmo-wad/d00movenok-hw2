from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str = Field(...)


class Error(BaseModel):
    error: str = Field(...)
