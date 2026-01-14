from pydantic import BaseModel, EmailStr
from datetime import datetime


# Request schemas
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


# Response schemas
class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Working with users
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
