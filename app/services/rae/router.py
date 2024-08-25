from fastapi import APIRouter

from app.schemas.word_model import WordModel
from app.services.rae.fetch_word_from_website import fetch_word_from_website
from app.services.rae.manager import fetch_word

rae_router: APIRouter = APIRouter(prefix="/rae", tags=["RAE"])


@rae_router.get("/word/")
def get_word(name: str) -> WordModel:
    """
    Get a word of the RAE and return it's definitions.

    :return: the word with it's fields
    :rtype: WordModel
    """
    return fetch_word(name=name)
