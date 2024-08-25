from requests import Response
from starlette import status

from app.schemas.word_model import WordModel
from app.services.rae.fetch_word_from_website import parse_response_into_word
from unittest.mock import Mock

from app.shared.utils import read_file


def test_parse_response_into_word() -> None:
    """
    Unit test that converts a Response into a Word, making it easier.
    """
    mock_response = Mock(spec=Response)
    mock_response.text = read_file("./gato_definition.html")
    mock_response.status_code = status.HTTP_200_OK
    word_response: WordModel = parse_response_into_word(response=mock_response, name='gato',
                                                        final_url='https://dle.rae.es/gato')

    word_expected: WordModel = WordModel(
        name="gato1, ta",
        definitions=[
            "1. m. y f. Mamífero de la familia de los félidos, digitígrado, doméstico, de unos 50 cm de largo desde la cabeza hasta el arranque de la cola, que por sí sola mide unos 20 cm, de cabeza redonda, lengua muy áspera, patas cortas y generalmente pelaje suave y espeso, de color blanco, gris, pardo, rojizo o negro, empleado en algunos lugares para cazar ratones. U. en m. ref. a la especie.Sin.:minino, michino, cucho2, micho, morrongo, morroño, mozo1.",
            '5. m. Máquina que sirve para levantar grandes pesos a poca altura, y que funciona con un engranaje y un trinquete de seguridad, o con una tuerca y un husillo.Sin.:elevador, palanca, cric.'],
        url='https://dle.rae.es/gato'
    )

    assert word_response == word_expected
