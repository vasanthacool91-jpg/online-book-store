from sqlmodel import SQLModel

class WishlistCreate(SQLModel):
    user_id: int
    book_id: int