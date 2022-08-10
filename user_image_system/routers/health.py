from datetime import datetime
from typing import Dict

from fastapi import APIRouter

health_router = APIRouter()


@health_router.get('', summary='Is the API is healthy?')
def alive() -> Dict[str, datetime]:
    return {'timestamp': datetime.now()}


@health_router.get('/live', summary='Is the API live?')
def live() -> str:
    return 'LIVE'


@health_router.get('/ready', summary='Is the API ready?')
def ready() -> str:
    return 'READY'
