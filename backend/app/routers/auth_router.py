from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import User
from app.schemas import UserRegister, UserLogin
from app.auth import hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user: UserRegister, session: Session = Depends(get_session)):
    existing_user = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return {
        "message": "User registered successfully",
        "user": db_user
    }


@router.post("/login")
def login(user: UserLogin, session: Session = Depends(get_session)):
    db_user = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }