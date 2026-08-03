from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database import get_session
from app.schemas import BookCreate
from app.services import book_service

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get("/")
def get_books(session: Session = Depends(get_session)):
    return book_service.get_all_books(session)


@router.get("/{book_id}")
def get_book(book_id: int, session: Session = Depends(get_session)):
    book = book_service.get_book(book_id, session)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("/")
def create_book(book: BookCreate, session: Session = Depends(get_session)):
    return book_service.create_book(book, session)


@router.put("/{book_id}")
def update_book(book_id: int, book: BookCreate, session: Session = Depends(get_session)):
    updated_book = book_service.update_book(book_id, book, session)

    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book


@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    deleted = book_service.delete_book(book_id, session)

    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted successfully"}