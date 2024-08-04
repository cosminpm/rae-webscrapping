from fastapi import APIRouter

from app.schemas.word_model import Word
from app.services.rae.get_word import fetch_word

rae_router: APIRouter = APIRouter(prefix="/rae", tags=["RAE"])


@rae_router.get("/word/")
def get_word(name: str) -> Word:
    """
    Get a word of the RAE and return it's definitions.

    :return: the word with it's fields
    :rtype: Word
    """
    return fetch_word(name=name)
