from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.operations.models import Operation

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    """
    Функция возвращает список операций с конкретным типом, заданным пользователем
    """
    q = select(Operation).filter(Operation.type == operation_type)
    result = await session.execute(q)
    operations = result.mappings().all()
    return operations


