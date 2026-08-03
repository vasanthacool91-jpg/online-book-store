from fastapi import HTTPException
from sqlmodel import Session, select

from app.models import Wishlist
from app.schemas import WishlistCreate


def add_to_wishlist(wishlist: WishlistCreate, session: Session):
    db = Wishlist(**wishlist.model_dump())

    session.add(db)
    session.commit()
    session.refresh(db)

    return db


def get_wishlist(user_id: int, session: Session):
    return session.exec(
        select(Wishlist).where(Wishlist.user_id == user_id)
    ).all()


def delete_wishlist(wishlist_id: int, session: Session):
    wishlist = session.get(Wishlist, wishlist_id)

    if not wishlist:
        raise HTTPException(status_code=404, detail="Wishlist not found")

    session.delete(wishlist)
    session.commit()

    return {
        "message": "Removed successfully"
    }