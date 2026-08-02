from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables
from app.routers.auth_router import router as auth_router
from app.routers.book_router import router as book_router
from app.routers.wishlist_router import router as wishlist_router
from app.routers.cart_router import router as cart_router



app = FastAPI(title="Online Book Store API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    create_db_and_tables()

app.include_router(auth_router)
app.include_router(book_router)
app.include_router(wishlist_router)
app.include_router(cart_router)

@app.get("/")
def home():
    return {"message": "Online Book Store API"}