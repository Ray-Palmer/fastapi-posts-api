from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import post, user, auth

# uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs

models.Base.metadata.create_all(bind=engine)  # Create models

app = FastAPI()

app.include_router(post.router)  # include post routes
app.include_router(user.router)  # include user routes
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Welcome to my api"}
