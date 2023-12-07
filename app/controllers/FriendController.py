from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password
from app.controllers.BaseController import BaseController
from app.models.Friend import Friend
from app.schemas.Friend import FriendCreate, FriendUpdate


class FriendController(BaseController[Friend, FriendCreate, FriendUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Friend]:
        return db.query(Friend).filter(Friend.email == email).first()

    def create(self, db: Session, *, obj_in: FriendCreate) -> Friend:
        db_obj = Friend(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            Friendname=obj_in.Friendname,
            is_superFriend=obj_in.is_superFriend,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Friend, obj_in: Union[FriendUpdate, Dict[str, Any]]
    ) -> Friend:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[Friend]:
        friend = self.get_by_email(db, email=email)
        if not friend:
            return None
        if not verify_password(password, friend.hashed_password):
            return None
        return friend

    def is_active(self, friend: Friend) -> bool:
        return friend.is_active

    def is_superFriend(self, friend: Friend) -> bool:
        return friend.is_superFriend


friend_controller = FriendController(Friend)