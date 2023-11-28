from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class UserModel(Base):
    __tablename__ = "users"

    # setting index to true makes id, username, and email easier to search amongst large data
    id = Column(Integer, primary_key=True, index=True)
    # not allowing null so users must have a username
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    # don't think I need the is_superuser code below
    # is_superuser = Column(Boolean(), default=False)
    relationship()

    def to_schema(self):
        return UserInDB(
            id=self.id,
            username=self.username,
            email=self.email,
            hashed_password=self.hashed_password,
            is_active=self.is_active,
            # don't think I need the is_superuser code below
            # is_superuser=self.is_superuser
        )
class MessageModel(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message_content = Column(String, nullable=False)
    sent_at = Column(DateTime, nullable=False)
