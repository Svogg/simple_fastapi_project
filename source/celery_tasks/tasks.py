from celery import Celery
from fastapi import Depends
from source.database import User

celery = Celery('tasks', broker='redis://localhost:6379')


def say_to(user=Depends(User)):
    return {
        'status': 200,
        'response': 'delyaed Hello to {} :)'.format(user.username)
    }
