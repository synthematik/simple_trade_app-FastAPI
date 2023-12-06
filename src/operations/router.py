from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.operations.models import Operation
from src.operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


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


@router.post("/")
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

