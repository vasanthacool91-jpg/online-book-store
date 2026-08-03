from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.schemas import CartCreate
from app.services import cart_service

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post("/")
def add_to_cart(cart: CartCreate, session: Session = Depends(get_session)):
    return cart_service.add_to_cart(cart, session)


@router.get("/{user_id}")
def get_cart(user_id: int, session: Session = Depends(get_session)):
    return cart_service.get_cart(user_id, session)


@router.put("/{cart_id}")
def update_cart(cart_id: int, quantity: int, session: Session = Depends(get_session)):
    return cart_service.update_cart(cart_id, quantity, session)


@router.delete("/{cart_id}")
def delete_cart(cart_id: int, session: Session = Depends(get_session)):
    return cart_service.delete_cart(cart_id, session)