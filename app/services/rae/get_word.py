import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException
from starlette import status

from app.schemas.word_model import Word

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 [ip:5.91.168.176]"
}


def get_word(palabra: str):
    base_url = "https://dle.rae.es/"
    final_url = base_url + palabra

    response = requests.get(final_url, headers=HEADERS)
    status_code = response.status_code

    def get_definitions(s: BeautifulSoup) -> list[str]:
        defs = s.select('p[class^="j"]')
        return [definition.get_text() for definition in defs]

    if status_code == status.HTTP_200_OK:
        soup = BeautifulSoup(response.text)
        name = soup.find("header").text
        definitions = get_definitions(s=soup)

        return Word(name=name,
                    definitions=definitions,
                    url=final_url)

    elif status_code == status.HTTP_400_BAD_REQUEST:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"There was an error in your request probably the word {palabra} does not exist.")
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"There was an unexpected error.")


if __name__ == '__main__':
    word = get_word("perro")
    ...
