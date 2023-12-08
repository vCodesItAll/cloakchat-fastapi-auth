from fastapi import APIRouter, Depends, Form, HTTPException, status
from app import db
from app.models import Friends, User, token
from fastapi import APIRouter, Depends, HTTPException, status
from app import db, models, schemas, controllers
from app.api.deps import get_current_user
from typing import Annotated
from sqlalchemy.orm import Session
from app.api import deps

router = APIRouter()

def get_friend_by_id(friend_id: int):
    friend = db.query(Friends).filter(Friends.id == friend_id).first()
    return friend

def get_current_friend():
    return None

# @router.post("/add-friend/{friend_id}")
# def add_friend(*, db: Session = Depends(deps.get_db), friend_id: Annotated[int, Form()], current_user: models.User = Depends(get_current_user(db, token))):
#     friend = get_friend_by_id(friend_id)
#     if friend:
#         # Add a friendship entry for the current user and the friend
#         db_friendship = Friends(user_id=current_user.id, friend_id=friend.id)
#         db.add(db_friendship)
#         db.commit()
#         return {"message": "Friend added successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Friend not found")
    
    # def get_child_by_unique_code(self, db: Session, unique_child_code: str) -> Optional[Child]:
    #     return db.query(self.model).filter(self.model.unique_child_code == unique_child_code).first
