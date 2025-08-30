import datetime
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy import event
from sqlmodel import Session, select

from .database import get_session, init_db
from .models import BaseUser, User


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    print("Shutting down...")


@event.listens_for(User, "before_update")
def update_timestamp(mapper, connection, target):
    target.updated_at = datetime.datetime.now(datetime.timezone.utc)


app = FastAPI(debug=True, lifespan=lifespan)


# Root endpoint
@app.get("/")
def root():
    return {"message": "Hello, FastAPI + SQLModel + PostgreSQL!"}


# Tworzenie użytkownika
@app.post("/users/", response_model=User)
def create_user(user: BaseUser, session: Session = Depends(get_session)):
    new_user = User(name=user.name)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


# Pobranie wszystkich użytkowników
@app.get("/users/", response_model=list[User])
def get_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users
