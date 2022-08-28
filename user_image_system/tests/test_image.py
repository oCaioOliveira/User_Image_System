from utils.crud import filter_image
from routers.image import get_filter_images_by_ids
import pytest

def test_filter_image(mocker):
    returned_value = {
        'base_64': 'string',
        'image_id': '1'
    }
    mocker.patch('utils.crud.retrieve_image_with_id', return_value = returned_value)
    response = filter_image({}, 1, 1)
    assert len(response) == 1
    assert response[0] == returned_value
    
def test_get_filter_images_by_ids(mocker):
   returned_value = {
       'base_64': 'string',
       'image_id': '1'
   }
   fake_response = [{
       'base_64': 'string',
       'image_id': '1'
   }]
   mocker.patch('utils.crud.retrieve_image_with_id', return_value = returned_value)
   response = get_filter_images_by_ids(1, 1, {})
   assert response == fake_response

def test_get_filter_images_by_ids_error(mocker):
   returned_value = []
   mocker.patch('utils.crud.retrieve_image_with_id', return_value = returned_value)
   mocker.patch('utils.crud.filter_image', return_value = returned_value)
   with pytest.raises(Exception):
       get_filter_images_by_ids(39, 40, {})

