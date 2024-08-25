from app.infraestructure.database.word import Word
from app.shared.unit_of_work import UnitOfWork


def create_tables():
    with UnitOfWork() as uow:
        engine = uow.engine
        Word.__table__.create(engine)


if __name__ == '__main__':
    create_tables()
