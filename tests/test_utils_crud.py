from user_image_system.utils.crud import update_user, remove_user, create_user
from user_image_system.utils.datatypes import UpdateImageValuesType, UpdateUserValuesType
from user_image_system.models.models import User, Image
from user_image_system.utils.errors import userNotFound, imageNotFound
from user_image_system.schemas.schemas import CreateImageSchema, CreateUserSchema, UpdateUserSchema

from random import randint

import pytest
from uuid import uuid4

def test_insert_user(db_conn):
    assert isinstance(create_user(db_conn, CreateUserSchema(name='Olasd')), User)

@pytest.mark.parametrize("test_id,updateValues,insert_b4,expected", [(1, {'name': 'paulo'}, True, User)])
def test_update_user(db_conn, test_id, updateValues: UpdateUserValuesType, insert_b4:bool, expected):
    
    if insert_b4:
        create_user(db_conn, CreateUserSchema(name=str(uuid4())))
    
    assert isinstance(update_user(db_conn, test_id, updateValues), expected)


# @pytest.mark.parametrize("test_id,updateValues,expected", [(2, UpdateUserSchema(name="Ola"), User), (1, UpdateUserSchema(name='Paulos'), User)])
def test_invalid_update_user(db_conn):
    
    with pytest.raises(userNotFound):
        update_user(db_conn, randint(0, 2500), {"name": "Paulo"})


def test_remove_user(db_conn):
    
    assert remove_user(db_conn, 1)

def test_invalid_remove_user(db_conn):

    with pytest.raises(userNotFound):
        remove_user(db_conn, 1)