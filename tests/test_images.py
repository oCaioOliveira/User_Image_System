from user_image_system.utils.crud import update_user, remove_user, create_user
from user_image_system.utils.datatypes import UpdateImageValuesType, UpdateUserValuesType
from user_image_system.models.models import User, Image
from user_image_system.utils.errors import userNotFound, imageNotFound
from user_image_system.schemas.schemas import CreateImageSchema, CreateUserSchema, UpdateUserSchema

from pathlib import Path

from random import randint

import pytest
from uuid import uuid4


@pytest.mark.parametrize("initial_id,final_id", [(1, 5)])
def test_imgs_filter(db_conn_with_images, initial_id, final_id):
    from base64 import b64encode
    import os
    from user_image_system.routers.image import get_list_of_images_with_filter
    
    from user_image_system.models.models import Image
    imgs_path = Path(__file__).parent.joinpath('./images')
    images:list[(int, bytes)] = []
    for index, img in enumerate(os.listdir(imgs_path)):
        images.append((index+1, b64encode(open(imgs_path.joinpath(img), 'rb').read())))
    
    response_images = get_list_of_images_with_filter(initial_id, final_id, db=db_conn_with_images)
    
    assert len(images) == len(response_images)
    
    for image, correct_image in zip(response_images, images):
        assert isinstance(image, Image)
        assert image.image_id == correct_image[0]
        assert image.base_64 == correct_image[1].decode('utf-8')