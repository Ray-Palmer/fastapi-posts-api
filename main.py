from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

# uvicorn main:app --reload


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # If not provided, than use default value = True
    rating: Optional[int] = None  # Optional field


my_posts = [
    {"title": "The title", "content": "Some interesting content of this post", "id": 1}
]


def find_post(id: int) -> dict:
    for post in my_posts:
        if post["id"] and post["id"] == id:
            return post


@app.get("/")
def root():
    return {"message": "Welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id: {id} was not found."}
        # OR USE HTTPEXCEPTION
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} was not found.",
        )
    return {"post_detail": post}
