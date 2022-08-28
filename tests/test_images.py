from user_image_system.utils.crud import update_user, remove_user, create_user
from user_image_system.utils.datatypes import UpdateImageValuesType, UpdateUserValuesType
from user_image_system.models.models import User, Image
from user_image_system.utils.errors import userNotFound, imageNotFound
from user_image_system.schemas.schemas import CreateImageSchema, CreateUserSchema, UpdateUserSchema

from pathlib import Path

from random import randint

import pytest
from uuid import uuid4


@pytest.mark.parametrize("initial_id,final_id", [(0, 5)])
def test_imgs_filter(db_conn_with_images, initial_id, final_id):
    from base64 import b64encode
    import os
    
    imgs_path = Path(__file__).parent.joinpath('./images')
    images = []
    for index, img in enumerate(os.listdir(imgs_path)):
        images.append((index, b64encode(open(imgs_path.joinpath(img), 'rb').read())))
    
    response = get_list_of_images_with_filter(initial_id, final_id)
    
    assert len(images) == len(response)
    
    for curr_id, b64img in response:
        assert b64img == response[1]
        assert curr_id == response[0]