from fastapi import HTTPException

import uuid
import re
from pydantic import BaseModel, EmailStr, field_validator


# API Model, FormRequest\Resource

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        orm_mode = True  # All JSON


# Resource

class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    is_active: bool


# FormRequest

class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr

    @field_validator('name')
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name should contains only letter"
            )
        return value

    @field_validator('surname')
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Surname should contains only letter"
            )
        return value
