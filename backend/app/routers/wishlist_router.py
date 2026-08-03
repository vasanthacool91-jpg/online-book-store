from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.database import get_session
from app.schemas import WishlistCreate
from app.services import wishlist_service

router = APIRouter(
    prefix="/wishlist",
    tags=["Wishlist"]
)


@router.post("/")
def add_to_wishlist(
    wishlist: WishlistCreate,
    session: Session = Depends(get_session)
):
    return wishlist_service.add_to_wishlist(wishlist, session)


@router.get("/{user_id}")
def get_wishlist(
    user_id: int,
    session: Session = Depends(get_session)
):
    return wishlist_service.get_wishlist(user_id, session)


@router.delete("/{wishlist_id}")
def delete_wishlist(
    wishlist_id: int,
    session: Session = Depends(get_session)
):
    return wishlist_service.delete_wishlist(wishlist_id, session)