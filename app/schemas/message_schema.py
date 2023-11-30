from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class MessageSchemaBase(BaseModel):
    message_content: str
    sender_id: int
    receiver_id: int

    class Config:
        from_attributes = True

class MessageCreate(MessageSchemaBase):
    message_content: str

class MessageInDBBase(MessageSchemaBase):
    id: int
    sent_at: datetime

# # Pydantic model for creating a new message
# class MsgCreate(BaseModel):
#     sender_id: int
#     receiver_id: int
#     message_content: str

#     class Config:
#         orm_mode = True
