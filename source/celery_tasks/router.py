from fastapi import APIRouter, Depends
from source.database import User

from .tasks import say_to

router = APIRouter(prefix='/data')


@router.get('/report')
def get_report(user=Depends(User)):
    say_to.delay(user.username)
    return {
        'status': 200,
        'data': 'celery вернул задачу от пользователя {}'.format(user.username),
        'details': None
    }
