from fastapi import APIRouter, Depends, HTTPException, status
from app import db
from app.models import Friends, User
from app.database import get_db

router = APIRouter()

@router.post("/add-friend/{friend_id}")
def add_friend(friend_id: int, current_user: User = Depends(get_current_friend)):
    friend = get_friend_by_id(friend_id)
    if friend:
        # Add a friendship entry for the current user and the friend
        db_friendship = Friends(user_id=current_user.id, friend_id=friend.id)
        db.add(db_friendship)
        db.commit()
        return {"message": "Friend added successfully"}
    else:
        raise HTTPException(status_code=404, detail="Friend not found")
