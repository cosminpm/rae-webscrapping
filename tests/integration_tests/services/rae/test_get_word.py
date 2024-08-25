from app.schemas.word_model import WordModel
from app.services.rae.router import get_word


def test_parse_response_into_word() -> None:
    """
    Integration test that converts a Response into a Word
    """
    word: WordModel = get_word(name="gato")
    expected_definitions: set = {
        "1. m. y f. Mamífero de la familia de los félidos, digitígrado, doméstico, de unos 50 cm de largo desde la cabeza hasta el arranque de la cola, que por sí sola mide unos 20 cm, de cabeza redonda, lengua muy áspera, patas cortas y generalmente pelaje suave y espeso, de color blanco, gris, pardo, rojizo o negro, empleado en algunos lugares para cazar ratones. U. en m. ref. a la especie.Sin.:minino, michino, cucho2, micho, morrongo, morroño, mozo1.",
        '5. m. Máquina que sirve para levantar grandes pesos a poca altura, y que funciona con un engranaje y un trinquete de seguridad, o con una tuerca y un husillo.Sin.:elevador, palanca, cric.'}
    assert word.name == "gato1, ta"
    assert len(word.definitions) >= 2
    response_definitions: set = set(word.definitions)
    assert expected_definitions.issubset(response_definitions)
