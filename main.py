from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # If not provided, than use default value = True
    rating: Optional[int] = None  # Optional field


@app.get("/")
def root():
    return {"message": "Welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)  # PyDentic instance
    print(post.dict())  # Convert to python dict
    print(post.title)
    print(post.published, post.rating)
    return {"data": "new post created"}
