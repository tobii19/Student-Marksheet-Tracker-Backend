from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:meeto1904%40@localhost:5555/fapi"

engine = create_engine(DB_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        