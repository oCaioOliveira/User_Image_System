from email.generator import Generator
from turtle import update
from typing import Dict, List, Optional, Union
from fastapi import(
    Depends,
    FastAPI, 
    HTTPException,
    Response, 
    status
)
from sqlalchemy.orm import Session
from crud import *
from database import Base, SessionLocal, engine
from datatypes import *
from datetime import datetime
from schemas import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def welcome() -> str:
    return {"Welcome!"}


@app.get("/health/")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}


@app.get("/users/", status_code=status.HTTP_200_OK,)
def get_all_users(db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_users(db):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem usuários cadastrados."
    )


@app.get("/users/{user_id}/", status_code=status.HTTP_200_OK,)
def get_user_with_id(user_id: int, db: Session = Depends(get_db)) -> UserType:
    if result := retrieve_user_with_id(db, user_id):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Usuário de 'id={user_id}' não encontrado."
    )


@app.delete("/users/{user_id}/", status_code=status.HTTP_204_NO_CONTENT,)
def delete_user(user_id: int, db: Session = Depends(get_db)) -> None:
    if not remove_user(db, user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuário de 'id={user_id}' não encontrado.",
        )


@app.post("/users/", status_code=status.HTTP_201_CREATED,)
def post_user(user: CreateUserSchema, db: Session = Depends(get_db),) -> UserType:
    if result := create_user(db, user):
        return result
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


@app.put("/users/{user_id}", status_code=status.HTTP_201_CREATED)
def put_user(user_id: int, user: UpdateUserSchema, db: Session = Depends(get_db)) -> UserType:
    if result := update_user(
        db, user_id, {
            key: value for key, value in user if value
        },
    ):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Usuário de 'id={user_id}' não encontrado.",
    )


@app.get("/images/", status_code=status.HTTP_200_OK,)
def get_all_images(db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_all_images(db):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem imagens cadastradas."
    )


@app.get("/images/{user_id}", status_code=status.HTTP_200_OK,)
def get_all_images_from_user(user_id: int, db: Session = Depends(get_db)) -> Generator:
    if result := retrieve_images_with_user_id(db, user_id):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem imagens cadastradas."
    )


@app.get("/images/{image_id}/", status_code=status.HTTP_200_OK,)
def get_image_with_id(image_id: int, db: Session = Depends(get_db)) -> ImageType:
    if result := retrieve_image_with_id(db, image_id):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Imagem de 'id={image_id}' não encontrada."
    )


@app.delete("/images/{image_id}/", status_code=status.HTTP_204_NO_CONTENT,)
def delete_image(image_id: int, db: Session = Depends(get_db)) -> None:
    if not remove_image(db, image_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Imagem de 'id={image_id}' não encontrada.",
        )

    
@app.post("/images/", status_code=status.HTTP_201_CREATED,)
def post_image(image: CreateImageSchema, db: Session = Depends(get_db),) -> ImageType:
    if result := create_image(db, image):
        return result
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


@app.put("/images/{image_id}", status_code=status.HTTP_201_CREATED)
def put_image(image_id: int, image: UpdateImageSchema, db: Session = Depends(get_db)) -> ImageType:
    if result := update_image(
        db, image_id, {
            key: value for key, value in image if value
        },
    ):
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Imagem de 'id={image_id}' não encontrada.",
    )