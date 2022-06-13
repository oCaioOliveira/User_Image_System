from typing import Any
from pydantic import BaseModel

class UserBaseSchema(BaseModel):
    name: str


class CreateUserSchema(UserBaseSchema):
    pass


class UserSchema(UserBaseSchema):
    user_id: int


class UpdateUserSchema(UserBaseSchema):
    name: str = ""


class ImageBaseSchema(BaseModel):
    user_id: int
    base_64: str


class CreateImageSchema(ImageBaseSchema):
    pass


class ImageSchema(ImageBaseSchema):
    image_id: int


class UpdateImageSchema(ImageBaseSchema):
    base_64: str = ""