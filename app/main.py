from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import post, user, auth, votes

# uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs

app = FastAPI()

origins = ["*"]  # Every domain can reach out to my API

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)  # include post routes
app.include_router(user.router)  # include user routes
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def root():
    return {"message": "Welcome to my api"}
