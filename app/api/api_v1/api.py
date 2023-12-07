from fastapi import APIRouter

from app.api.api_v1.endpoints import friend, login, users, utils

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# app.include_router(friends.router, prefix="/api/friends", tags=["friends"])
api_router.include_router(friend.router, prefix="/friends", tags=["friends"])