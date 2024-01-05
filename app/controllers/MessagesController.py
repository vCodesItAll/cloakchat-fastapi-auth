from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password
from app.controllers.BaseController import BaseController
from app.models import MessageModel
from app.schemas.message_schema import MessageCreate, MessageInDBBase
from datetime import datetime

class MessagesController(BaseController[MessageModel, MessageCreate, MessageInDBBase]):
    def get_messages(self, db: Session) -> Optional[MessageModel]:
        return db.query(MessageModel).all()

    def create(self, db: Session, obj_in: MessageCreate) -> MessageModel:
        db_obj = MessageModel(
            sender_id=obj_in.sender_id,
            receiver_id=obj_in.receiver_id,
            message_content=obj_in.message_content,
            sent_at=datetime.utcnow()  
            # find out the correct import for datetime and you should be set    
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def update(
    #     self, db: Session, *, db_obj: MessageModel, obj_in: Union[MessageUpdate, Dict[str, Any]]
    # ) -> MessageModel:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     if update_data["password"]:
    #         hashed_password = get_password_hash(update_data["password"])
    #         del update_data["password"]
    #         update_data["hashed_password"] = hashed_password
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)

    # def authenticate(self, db: Session, *, email: str, password: str) -> Optional[MessageModel]:
    #     user = self.get_by_email(db, email=email)
    #     if not user:
    #         return None
    #     if not verify_password(password, user.hashed_password):
    #         return None
    #     return user

    # def is_active(self, user: MessageModel) -> bool:
    #     return user.is_active

    # def is_superuser(self, user: MessageModel) -> bool:
    #     return user.is_superuser


msg = MessagesController(MessageModel)