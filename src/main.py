from src.auth.auth import auth_backend
from fastapi import FastAPI, Depends
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreate
from src.auth.auth import fastapi_users
from src.operations.router import router as router_operation
from src.task.router import router as router_task
from src.pages.router import router as router_pages
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis
from starlette.staticfiles import StaticFiles

app = FastAPI(
    title="Trade App"
)

app.mount("/static", StaticFiles(directory="src/static"), name="static")


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


app.include_router(router_task)

app.include_router(router_pages)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


@app.get("/unprotected-route")
def unprotected_route(user: User = Depends(current_user)):
    return f"Hello, anonim"


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
