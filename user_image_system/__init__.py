from fastapi import FastAPI

from routers.health import health_router
from routers.start import start_router
from routers.user import user_router
from routers.image import image_router


def create_app() -> FastAPI:
    app = FastAPI(
        title='User Image System',
        description='This system is used for control users and your images.'
    )

    app.include_router(start_router, tags=['Start'])
    app.include_router(health_router, prefix='/health', tags=['Health'])
    app.include_router(user_router, prefix='/user', tags=['User'])
    app.include_router(image_router, prefix='/image', tags=['Image'])

    return app