from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils, add_friend

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# app.include_router(friends.router, prefix="/api/friends", tags=["friends"])
api_router.include_router(add_friend.router, prefix="/friends", tags=["friends"])