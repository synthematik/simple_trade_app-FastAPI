from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter, BackgroundTasks, Depends

from src.auth.auth import current_user

from src.task.tasks import send_email

router = APIRouter(
    prefix="/tasks",
    tags=["Task"]
)


@router.get("/dashboard")
def get_dashboard(user=Depends(current_user)):
    """
    Функция отправляет пользователю письмо на почту. Используется Redis + Celery
    """
    try:
        send_email.delay(user.username)
        return {
            "status": 200,
            "data": "Письмо отправлено",
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
