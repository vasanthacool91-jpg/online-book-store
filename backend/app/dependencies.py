from fastapi import Depends
from sqlmodel import Session
from app.database import get_session

def get_db():
    return Depends(get_session)