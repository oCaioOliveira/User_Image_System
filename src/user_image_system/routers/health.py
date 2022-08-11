from fastapi import APIRouter
from datetime import datetime
from typing import Dict

health_router = APIRouter()


@health_router.get('', summary='Is the API is healthy?')
def alive() -> Dict[str, datetime]:
    return {'timestamp': datetime.now()}


@health_router.get('/live', summary='Is the API live?')
def alive() -> str:
    return 'LIVE'


@health_router.get('/ready', summary='Is the API ready?')
def alive() -> str:
    return 'READY'