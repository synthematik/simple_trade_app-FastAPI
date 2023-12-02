from datetime import datetime
from enum import Enum

from fastapi import FastAPI, Request, status
from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Trade App"
)


@app.get('/')
async def root():
    return "Hello world"
