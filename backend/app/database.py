from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///bookstore.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

def create_db_and_tables():
    import app.models
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session