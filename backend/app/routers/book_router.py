from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.database import get_session
from app.models import Book
from app.schemas import BookCreate

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("/")
def add_book(book: BookCreate, session: Session = Depends(get_session)):
    db_book = Book(**book.model_dump())
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

@router.get("/")
def get_books(session: Session = Depends(get_session)):
    return session.exec(select(Book)).all()

@router.get("/search/")
def search_books(search: str, session: Session = Depends(get_session)):
    return session.exec(
        select(Book).where(Book.title.contains(search))
    ).all()

@router.put("/{book_id}")
def update_book(book_id: int, book: BookCreate, session: Session = Depends(get_session)):
    db_book = session.get(Book, book_id)

    if not db_book:
        return {"message": "Book not found"}

    db_book.title = book.title
    db_book.author = book.author
    db_book.category = book.category
    db_book.price = book.price
    db_book.description = book.description
    db_book.image = book.image

    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book


@router.delete("/{book_id}")
def delete_book(book_id: int, session: Session = Depends(get_session)):
    book = session.get(Book, book_id)

    if not book:
        return {"message": "Book not found"}

    session.delete(book)
    session.commit()

    return {"message": "Book deleted successfully"}