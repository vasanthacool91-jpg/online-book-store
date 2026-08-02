from sqlmodel import SQLModel

class BookCreate(SQLModel):
    title: str
    author: str
    category: str
    price: float
    description: str
    image: str