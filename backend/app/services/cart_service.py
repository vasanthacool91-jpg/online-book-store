from fastapi import HTTPException
from sqlmodel import Session, select

from app.models import Cart
from app.schemas import CartCreate


def add_to_cart(cart: CartCreate, session: Session):
    db_cart = Cart(**cart.model_dump())

    session.add(db_cart)
    session.commit()
    session.refresh(db_cart)

    return db_cart


def get_cart(user_id: int, session: Session):
    return session.exec(
        select(Cart).where(Cart.user_id == user_id)
    ).all()


def update_cart(cart_id: int, quantity: int, session: Session):
    cart = session.get(Cart, cart_id)

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    cart.quantity = quantity

    session.commit()
    session.refresh(cart)

    return cart


def delete_cart(cart_id: int, session: Session):
    cart = session.get(Cart, cart_id)

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    session.delete(cart)
    session.commit()

    return {
        "message": "Item removed from cart"
    }