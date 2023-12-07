from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class Friends(Base):
    __tablename__ = "friends"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    friend_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", foreign_keys=[user_id])
    friend = relationship("User", foreign_keys=[friend_id])

    # Only one user has to add another to make them both friends
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'friend_id'),
    )
