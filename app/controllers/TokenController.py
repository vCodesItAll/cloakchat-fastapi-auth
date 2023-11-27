from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.controllers.BaseController import BaseController
from app.models.token import Token
from app.schemas.user import User

class TokenController(BaseController[Token, Token, Token]):
    def get_token_by_user_id(self, db: Session, *, obj_in: int) -> Optional[Token]:
        return db.query(Token).filter(Token.user_id == obj_in).first()
    
    def delete_inactive_tokens_by_user(self, db: Session, *, obj_in: int) -> Optional[User]:
        tokens = db.query(User).filter(Token.user_id == obj_in).all()
        stmt = delete(Token).where(Token.user_id.in_(tokens))
        db.execute(stmt)

        return db.query(User).filter(User.id == user_id).first()

    def create(self, db: Session, *, obj_in: str) -> Token:
        db_obj = Token(
            token_type = "bearer",
            access_token = obj_in
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def refresh(self, db: Session, *, obj_in: str) -> Token:
        db_obj: Token = db.query(Token).filter(Token.access_token == obj_in).first()
        
        # Check if the object was found
        if db_obj:
            # Update the desired fields with new data
            db_obj.expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)

            # Commit the changes to the database
            db.commit()

            # Refresh the instance to get the updated state from the database
            db.refresh(db_obj)

        return db_obj

token = TokenController(Token)