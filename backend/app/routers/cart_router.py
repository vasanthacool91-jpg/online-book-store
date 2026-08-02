from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import Cart
from app.schemas import CartCreate

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post("/")
def add_to_cart(cart: CartCreate, session: Session = Depends(get_session)):
    db_cart = Cart(**cart.model_dump())

    session.add(db_cart)
    session.commit()
    session.refresh(db_cart)

    return db_cart

@router.get("/{user_id}")
def get_cart(user_id: int, session: Session = Depends(get_session)):
    return session.exec(
        select(Cart).where(Cart.user_id == user_id)
    ).all()


@router.put("/{cart_id}")
def update_cart(
    cart_id: int,
    quantity: int,
    session: Session = Depends(get_session)
):
    cart = session.get(Cart, cart_id)

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    cart.quantity = quantity

    session.add(cart)
    session.commit()
    session.refresh(cart)

    return cart



@router.delete("/{cart_id}")
def delete_cart(cart_id: int, session: Session = Depends(get_session)):
    cart = session.get(Cart, cart_id)

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    session.delete(cart)
    session.commit()

    return {
        "message": "Item removed from cart"
    }