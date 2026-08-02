from sqlmodel import SQLModel
from pydantic import EmailStr

class UserRegister(SQLModel):
    name: str
    email: EmailStr
    password: str


class UserLogin(SQLModel):
    email: EmailStr
    password: str


class BookCreate(SQLModel):
    title: str
    author: str
    category: str
    price: float
    description: str
    image: str


class WishlistCreate(SQLModel):
    user_id: int
    book_id: int


class CartCreate(SQLModel):
    user_id: int
    book_id: int
    quantity: int
