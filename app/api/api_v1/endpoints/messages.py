from fastapi import APIRouter, HTTPException
from pytest import Session
from app.api import deps
from app import models, schemas, controllers
from typing import Dict, Any
from fastapi import APIRouter, Depends

# make endpoints - pass in object
router = APIRouter()

#this route accepts a json object called message
@router.post("/messages", response_model=schemas.message_schema.MessageInDBBase, status_code=201)
async def send_message(message: schemas.message_schema.MessageCreate, db: Session = Depends(deps.get_db)) -> Any:
    # this is where my controller stuff goes
    # sender = crud.get_user_by_id(db, message.sender_id)
    # receiver = crud.get_user_by_id(db, message.receiver_id)
    # 1. create the message model using the MessageController's create method
    new_message: models.MessageModel = controllers.msg.create(db, obj_in=message)
    # 2. convert the message model from the db to messageInDBase
    # message_schema = schemas.message_schema.MessageInDBBase(new_message)
    # 3. return the messageInDBBase
    return new_message

    

