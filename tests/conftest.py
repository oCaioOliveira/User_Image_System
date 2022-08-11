import pytest
from contextlib import closing

@pytest.fixture(scope='session')
def db_conn():
    from user_image_system.configs.database import SessionLocal
    from user_image_system.configs.database import db_path
    with SessionLocal as conn:
        yield conn

    db_path.unlink()
