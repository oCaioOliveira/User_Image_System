import pytest
from contextlib import closing

from random import Random

@pytest.fixture(scope='session')
def db_conn():
    from user_image_system.configs.database import SessionLocal
    from user_image_system.configs.database import db_path
    with SessionLocal as conn:
        yield conn

    db_path.unlink()
    


@pytest.fixture(scope='session')
def db_conn_with_images():
    from user_image_system.configs.database import SessionLocal
    from user_image_system.configs.database import db_path
    from random import randint, SystemRandom
    from string import ascii_letters, digits
    from base64 import b64encode
    from user_image_system.routers.image import create_image
    from user_image_system.schemas.schemas import CreateImageSchema
    from pathlib import Path
    import os
    
    imgs_path = Path(__file__).parent.joinpath('./images')

    for index, img in enumerate(os.listdir(imgs_path)):
        create_image(SessionLocal, CreateImageSchema(user_id=index, base_64=b64encode(open(imgs_path.joinpath(img), 'rb').read())))

    with SessionLocal as conn:
        yield conn

    db_path.unlink()
