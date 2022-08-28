from typing import Generator 
from sqlalchemy.orm import Session

from .datatypes import UpdateUserValuesType, UpdateImageValuesType

from models.models import User, Image
from schemas.schemas import CreateUserSchema, CreateImageSchema

users = User
images = Image

def create_user(db: Session, user: CreateUserSchema) -> User:
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def retrieve_all_users(db: Session) -> Generator:
    return db.query(users).all()


def retrieve_user_with_id(db: Session, user_id: int) -> User:
    if user := db.query(users).filter(users.user_id == user_id).first():
        return user
    return False 


def update_user(
    db: Session,
    user_id: int,
    values: UpdateUserValuesType
) -> User:
    if user := retrieve_user_with_id(db, user_id):
        db.query(users).filter(
            users.user_id == user_id
        ).update(values)
        db.commit()
        db.refresh(user)
        return user


def filter_user(
    db: Session,
    user_id_init: int,
    user_id_end: int
) -> Generator:
    list_users = []
    while(user_id_init <= user_id_end):
        if user := retrieve_user_with_id(db, user_id_init):
            list_users.append(user)
        user_id_init += 1
    return list_users


def remove_user(db: Session, user_id: int) -> bool:
    if user := retrieve_user_with_id(db, user_id):
        db.delete(user)
        db.commit()
        return True
    return False


def create_image(db: Session, image: CreateImageSchema) -> Image:
    new_image = Image(**image.dict())
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image


def retrieve_all_images(db: Session) -> Generator:
    return db.query(images).all()


def retrieve_image_with_id(db: Session, image_id: int):
    return db.query(images).filter(images.image_id == image_id).first()


def retrieve_images_with_user_id(db: Session, user_id: int) -> Generator:
    return db.query(images).filter(images.user_id == user_id).all()


def update_image(
    db: Session,
    image_id: int,
    values: UpdateImageValuesType
):
    if image := retrieve_image_with_id(db, image_id):
        db.query(images).filter(
            images.image_id == image_id
        ).update(values)
        db.commit()
        db.refresh(image)
        return image

def filter_image(
    db: Session,
    image_id_init: int,
    image_id_end: int
 ) -> Generator:
    list_images = []
    while(image_id_init <= image_id_end):
        if image := retrieve_image_with_id(db, image_id_init):
            list_images.append(image)
        image_id_init += 1
    return list_images


def remove_image(db: Session, image_id: int) -> bool:
    if image := retrieve_image_with_id(db, image_id):
        db.delete(image)
        db.commit()
        return True
    return False