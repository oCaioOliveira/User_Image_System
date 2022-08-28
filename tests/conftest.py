import pytest
from contextlib import closing

from random import Random

@pytest.fixture(scope='session')
def db_conn():
    from user_image_system.configs.database import SessionLocal
    with SessionLocal as conn:
        yield conn


@pytest.fixture(scope='session')
def db_conn_with_images():
    from user_image_system.configs.database import SessionLocal
    from base64 import b64encode
    from user_image_system.routers.image import create_image
    from user_image_system.routers.user import create_user
    from user_image_system.schemas.schemas import CreateImageSchema, CreateUserSchema
    from pathlib import Path
    import os
    
    imgs_path = Path(__file__).parent.joinpath('./images')
    with SessionLocal as conn:
        for img in os.listdir(imgs_path):
            r = create_user(conn, CreateUserSchema(name='Tste'))
            create_image(conn, CreateImageSchema(user_id=r.user_id, base_64=b64encode(open(imgs_path.joinpath(img), 'rb').read())))
        yield conn


def pytest_sessionfinish(session, exitstatus):
    from user_image_system.configs.database import db_path
    db_path.unlink()