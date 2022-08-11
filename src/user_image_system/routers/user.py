from sqlalchemy.orm import Session
from typing import Generator
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from ..configs.database import Base, SessionLocal, engine
from ..utils.datatypes import UserType
from ..schemas.schemas import UpdateUserSchema, CreateUserSchema
from ..utils.crud import (
    create_user,
    retrieve_all_users,
    retrieve_user_with_id,
    update_user,
    remove_user
    )

user_router = APIRouter()

Base.metadata.create_all(bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user_router.get("", status_code=status.HTTP_200_OK, summary='Get a list of all users')
def get_all_users(db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_users(db):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="There are no registered users."
    )


@user_router.post("", status_code=status.HTTP_201_CREATED, summary='Create user identifying with id')
def post_user(user: CreateUserSchema, db: Session = Depends(get_db),) -> UserType:
    if result := create_user(db, user):
        return result
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )



@user_router.get("/{user_id}", status_code=status.HTTP_200_OK, summary='Get an especific user by your id')
def get_user_with_id(user_id: int, db: Session = Depends(get_db)) -> UserType:
    if result := retrieve_user_with_id(db, user_id):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User of 'id={user_id}' not found."
    )


@user_router.put("/{user_id}", status_code=status.HTTP_201_CREATED, summary='Put a especific user by your id')
def put_user(user_id: int, user: UpdateUserSchema, db: Session = Depends(get_db)) -> UserType:
    if result := update_user(
        db, user_id, {
            key: value for key, value in user if value
        },
    ):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"User of 'id={user_id}' not found.",
    )


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary='Delete an especific user by your id')
def delete_user(user_id: int, db: Session = Depends(get_db)) -> None:
    if not remove_user(db, user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User of 'id={user_id}' not found.",
        )