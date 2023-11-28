from app.models.user_model import UserModel
from typing import Optional
from pydantic import BaseModel, EmailStr


class Msg(BaseModel):
    msg: str