from sqlalchemy import Engine
from sqlalchemy.orm import Session

from app.shared.session_local import SessionLocal, RaeEngine


class UnitOfWork:
    session: Session
    engine: Engine

    def __enter__(self):
        self.session = SessionLocal()
        self.engine = RaeEngine
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        if exc_val:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()
