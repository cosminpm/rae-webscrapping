import urllib.request
from http.client import HTTPResponse

from bs4 import BeautifulSoup
from fastapi import HTTPException
from starlette import status
from loguru import logger

from app.schemas.word_model import WordModel

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 [ip:5.91.168.176]"
}


def _fetch_word_from_rae(name: str) -> tuple[HTTPResponse, str]:
    base_url = "https://dle.rae.es/"
    final_url = base_url + name
    req = urllib.request.Request(final_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')

    return urllib.request.urlopen(req), final_url


def parse_response_into_word(response: HTTPResponse, name: str, final_url: str) -> WordModel:
    status_code = response.status
    logger.info(f"The response status code of the word: {name} was {status_code}.")

    def get_definitions(s: BeautifulSoup) -> list[str]:
        defs = s.select('p[class^="j"]')
        return [definition.get_text() for definition in defs]

    if status_code == status.HTTP_200_OK:
        text = response.read().decode('utf-8')
        soup = BeautifulSoup(text, features="html.parser")
        if (header := soup.find("header")) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The word '{name}' has not been found.")

        complete_name = header.text
        definitions = get_definitions(s=soup)

        return WordModel(name=complete_name,
                         definitions=definitions,
                         url=final_url)

    elif status_code == status.HTTP_400_BAD_REQUEST:
        logger.error(f"Error for word: {name}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"There was an error in your request probably the word '{name}' does not exist.")
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"There was an unexpected error.")


def fetch_word_from_website(name: str) -> WordModel:
    response, final_url = _fetch_word_from_rae(name)
    return parse_response_into_word(response=response, name=name, final_url=final_url)
