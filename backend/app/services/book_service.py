from sqlmodel import Session, select
from app.models import Book
from app.schemas import BookCreate


def get_all_books(session: Session):
    return session.exec(select(Book)).all()


def get_book(book_id: int, session: Session):
    return session.get(Book, book_id)


def create_book(book: BookCreate, session: Session):
    db_book = Book(**book.model_dump())

    session.add(db_book)
    session.commit()
    session.refresh(db_book)

    return db_book


def update_book(book_id: int, book: BookCreate, session: Session):
    db_book = session.get(Book, book_id)

    if not db_book:
        return None

    db_book.title = book.title
    db_book.author = book.author
    db_book.category = book.category
    db_book.price = book.price
    db_book.description = book.description
    db_book.image = book.image

    session.commit()
    session.refresh(db_book)

    return db_book


def delete_book(book_id: int, session: Session):
    db_book = session.get(Book, book_id)

    if not db_book:
        return False

    session.delete(db_book)
    session.commit()

    return True