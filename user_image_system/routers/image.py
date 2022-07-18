from sqlalchemy.orm import Session
from typing import Generator
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from utils.datatypes import ImageType
from schemas.schemas import UpdateImageSchema, CreateImageSchema
from .user import get_db 
from utils.crud import (
    retrieve_all_images,
    retrieve_images_with_user_id,
    retrieve_image_with_id,
    remove_image,
    create_image,
    update_image
)

image_router = APIRouter()


@image_router.get("", status_code=status.HTTP_200_OK, summary='Get a list of all images')
def get_all_images(db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_images(db):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="There are no registered images."
    )


@image_router.post("", status_code=status.HTTP_201_CREATED, summary='Create image identifying with id')
def post_image(image: CreateImageSchema, db: Session = Depends(get_db),) -> ImageType:
    if result := create_image(db, image):
        return result
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


@image_router.get("/{user_id}", status_code=status.HTTP_200_OK, summary='Get an especific image by your user id')
def get_all_images_from_user(user_id: int, db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_images_with_user_id(db, user_id):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="There are no registered images."
    )


@image_router.get("/{image_id}", status_code=status.HTTP_200_OK, summary='Get an especific image by your id')
def get_image_with_id(image_id: int, db: Session = Depends(get_db)) -> ImageType:
    if result := retrieve_image_with_id(db, image_id):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Image of 'id={image_id}' not found."
    )


@image_router.put("/{image_id}", status_code=status.HTTP_201_CREATED, summary='Put a especific image by your id')
def put_image(image_id: int, image: UpdateImageSchema, db: Session = Depends(get_db)) -> ImageType:
    if result := update_image(
        db, image_id, {
            key: value for key, value in image if value
        },
    ):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Image of 'id={image_id}' not found.",
    )


@image_router.delete("/{image_id}", status_code=status.HTTP_204_NO_CONTENT, summary='Delete an especific image by your id')
def delete_image(image_id: int, db: Session = Depends(get_db)) -> None:
    if not remove_image(db, image_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Image of 'id={image_id}' not found.",
        )