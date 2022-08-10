from fastapi import APIRouter

start_router = APIRouter()


@start_router.get("/", summary='Welcome to the API')
def welcome() -> str:
    return ('Welcome to the User Image System! For further information, read the documentation in /docs or /redoc.')
