from app.infraestructure.database.word import Word
from app.schemas.word_model import WordModel
from app.services.rae.fetch_word_from_website import fetch_word_from_website
from app.shared.unit_of_work import UnitOfWork


def fetch_word(name: str) -> WordModel:
    with UnitOfWork() as uow:
        orm = uow.session.query(Word).filter_by(name=name).first()
        if orm is None:
            word: WordModel = fetch_word_from_website(name)
            orm = Word(**word.model_dump())
            uow.session.add(orm)
            return word

        else:
            return WordModel.model_validate(orm)
