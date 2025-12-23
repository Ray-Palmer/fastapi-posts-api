from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(data: dict = Body):
    print(data)
    return {"new_post": f"title: {data['title']}, content: {data['content']}"}
