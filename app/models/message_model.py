from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class MessageModel(Base):
    __tablename__ = 'Messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message_content = Column(String, nullable=False)
    sent_at = Column(DateTime, nullable=False)