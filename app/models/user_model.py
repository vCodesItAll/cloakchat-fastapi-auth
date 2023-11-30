from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.schemas import UserInDB
from app.db.base_class import Base  # noqa

sender_association_table = Table('sent_messages', Base.metadata,
    Column('sender_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('receiver_id', Integer, ForeignKey('users.id'), primary_key=True)
)

receiver_association_table = Table('received_messages', Base.metadata,
    Column('sender_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('receiver_id', Integer, ForeignKey('users.id'), primary_key=True)
)
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
    is_superuser = Column(Boolean(), default=False)
    relationship()

    sent_messages = relationship(
        'UserModel', 
        secondary=sender_association_table,
        primaryjoin=id==sender_association_table.c.sender_id,
        secondaryjoin=id==sender_association_table.c.receiver_id,
        backref='sender_of'
    )

    received_messages = relationship(
       'UserModel', 
        secondary=receiver_association_table,
        primaryjoin=id==receiver_association_table.c.sender_id,
        secondaryjoin=id==receiver_association_table.c.receiver_id,
        backref='receiver_of'
    )

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


