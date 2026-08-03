from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.schemas import UserRegister, UserLogin
from app.services import auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserRegister,
    session: Session = Depends(get_session)
):
    return auth_service.register_user(user, session)


@router.post("/login")
def login(
    user: UserLogin,
    session: Session = Depends(get_session)
):
    return auth_service.login_user(user, session)