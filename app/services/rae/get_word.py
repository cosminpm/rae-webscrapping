import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException
from requests import Response
from starlette import status
from loguru import logger

from app.schemas.word_model import Word

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 [ip:5.91.168.176]"
}


def _fetch_word_from_rae(name: str) -> tuple[Response, str]:
    base_url = "https://dle.rae.es/"
    final_url = base_url + name
    return requests.get(final_url, headers=HEADERS), final_url


def _parse_response_into_word(response: Response, name: str, final_url: str) -> Word:
    status_code = response.status_code
    logger.info(f"The response status code of the word: {name} was {status_code}.")

    def get_definitions(s: BeautifulSoup) -> list[str]:
        defs = s.select('p[class^="j"]')
        return [definition.get_text() for definition in defs]

    if status_code == status.HTTP_200_OK:
        soup = BeautifulSoup(response.text, features="html.parser")
        complete_name = soup.find("header").text
        definitions = get_definitions(s=soup)

        return Word(name=complete_name,
                    definitions=definitions,
                    url=final_url)

    elif status_code == status.HTTP_400_BAD_REQUEST:
        logger.error(f"Error for word: {name}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"There was an error in your request probably the word {name} does not exist.")
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"There was an unexpected error.")


def fetch_word(name: str) -> Word:
    response, final_url = _fetch_word_from_rae(name)
    return _parse_response_into_word(response=response, name=name, final_url=final_url)

