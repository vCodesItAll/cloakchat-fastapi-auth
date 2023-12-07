from typing import Optional
from pydantic import BaseModel, EmailStr

# Shared properties
class FriendBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    username: Optional[str] = None

# Properties to receive via API on creation
class FriendCreate(FriendBase):
    email: EmailStr
    password: str

# Properties to receive via API on update
class UserUpdate(FriendBase):
    password: Optional[str] = None

class FriendInDBBase(FriendBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True

# Additional properties to return via API
class User(FriendInDBBase):
    pass

# Additional properties stored in DB
class UserInDB(FriendInDBBase):
    hashed_password: str