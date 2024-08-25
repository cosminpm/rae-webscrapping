from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f"sqlite:///database/rae.db"

RaeEngine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=RaeEngine)
