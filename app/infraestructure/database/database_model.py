from sqlalchemy.orm import DeclarativeBase


class DatabaseModel(DeclarativeBase):
    __abstract__ = True
