from pydantic import BaseModel, Field


class NewDescription(BaseModel):
    description: str = Field(...)


class NewPassword(BaseModel):
    old_password: str = Field(...)
    new_password: str = Field(..., min_length=9)
