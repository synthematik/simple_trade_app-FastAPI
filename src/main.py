from src.auth.auth import auth_backend
from fastapi import FastAPI, Depends
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreate
from src.auth.auth import fastapi_users
from src.operations.router import router as router_operation


app = FastAPI(
    title="Trade App"
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

app.include_router(router_operation)


current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def unprotected_route(user: User = Depends(current_user)):
    return f"Hello, anonim"
