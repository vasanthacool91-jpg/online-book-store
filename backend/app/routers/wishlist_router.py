from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import Wishlist
from app.schemas import WishlistCreate

router = APIRouter(
    prefix="/wishlist",
    tags=["Wishlist"]
)

@router.post("/")
def add_to_wishlist(
    wishlist: WishlistCreate,
    session: Session = Depends(get_session)
):
    db = Wishlist(**wishlist.model_dump())

    session.add(db)
    session.commit()
    session.refresh(db)

    return db


@router.get("/{user_id}")
def get_wishlist(
    user_id: int,
    session: Session = Depends(get_session)
):
    return session.exec(
        select(Wishlist).where(Wishlist.user_id == user_id)
    ).all()


@router.delete("/{wishlist_id}")
def delete_wishlist(
    wishlist_id: int,
    session: Session = Depends(get_session)
):
    wishlist = session.get(Wishlist, wishlist_id)

    if not wishlist:
        raise HTTPException(404, "Wishlist not found")

    session.delete(wishlist)
    session.commit()

    return {"message": "Removed successfully"}