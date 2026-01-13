from pydantic import BaseModel
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
        orm_mode = True
