from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class MessageModel(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message_content = Column(String, nullable=False)
    sent_at = Column(DateTime, nullable=False)

    # sender = relationship(
    #     'UserModel',
    #     back_populates='sent_messages')
    
    # receiver = relationship(
    #     'UserModel',
    #     back_populates='received_messages')