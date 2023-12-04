from auth.auth import auth_backend
from auth.manager import get_user_manager

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from models.models import User
from auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="Trade App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


@app.get('/')
async def root():
    return "Hello world"


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def unprotected_route(user: User = Depends(current_user)):
    return f"Hello, anonim"
