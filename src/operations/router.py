import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.operations.models import Operation
from src.operations.schemas import OperationCreate, OperationEdit
from starlette import status

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    """
    Просто проверка работоспособности redis
    """
    time.sleep(2)
    return "Some text"


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    """
    Функция возвращает список операций с конкретным типом, заданным пользователем
    """
    try:
        q = select(Operation).filter(Operation.type == operation_type)
        result = await session.execute(q)
        operations = result.mappings().all()
        return operations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    """
    Функция для записи данных в таблицу операций
    """
    try:
        stmt = insert(Operation).values(**new_operation.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status", "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
async def edit_some_operations(current_operation: OperationEdit, session: AsyncSession = Depends(get_async_session)):
    """
    Функция для изменения данных для конкретной операции. Также есть обработка ситуации, когда вводится несуществующий id
    """
    try:
        stmt = update(Operation).where(Operation.id == current_operation.id).values(**current_operation.dict())
        result = await session.execute(stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Operation not found")
        await session.commit()
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


