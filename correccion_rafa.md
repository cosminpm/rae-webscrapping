

# Correción CotizAPI
Puntos pequeños a corregir:
- Eliminar los emojis en el código, en el `reamde.md` está bien, pero en el propio código no: [Ejemplo](https://github.com/RafaelRemoteDev/CotizAPI/blob/main/main.py#L12)
- Debajo de la función `if __name__ == "__main__":` tienes que llamar a una función `main()` que tenga todo el código que has puesto ahí.
- En el `requirements.txt` es buena práctica poner un comentario alrededor de cada libreria diciendo para que sirve, por ejemplo: `telegram~=0.0.1 # Connect to Telegram and send messages.` así para cada uno.
- [Tienes el token de Telegram puesto en público](https://github.com/RafaelRemoteDev/CotizAPI/blob/main/.env#L2C1-L2C66), esto no puede ser así, tienes que usar un secreto que se almacene en GitHub.
- No añadas el `.idea` en el repositorio.
- [Cuando pones un error no pongas el número como tal](https://github.com/RafaelRemoteDev/CotizAPI/blob/main/api/endpoints.py#L75), en cambio usa esto:
    ```python
    from starlette import status
    status.HTTP_500_INTERNAL_SERVER_ERROR
    ```
- [En vez de usar `os.getenv("TELEGRAM_BOT_TOKEN")` usa el concepto](https://github.com/RafaelRemoteDev/CotizAPI/blob/main/bot/config_bot.py#L17C22-L17C53) que hemos explicado de crear un `config.py` que hemos explicado alguna vez en clase, que aunque no esté en el proyecto base, si que se ha explicado. [Ejemplo en un repositorio mio](https://github.com/cosminpm/bottle-caps-backend/blob/main/app/config.py).
- Una cosa mas: todas las funciones que puedan ser NO `async` hazlas "normales" es decir: `def ...` a no ser que tangas una justificación. Esto lo he corregido en la última clase, disculpa.
- [No uses prints](https://github.com/RafaelRemoteDev/CotizAPI/blob/main/db/database.py#L46), si quieres poner algo en la terminal de tu código usa la libreria `loguru` que la tienes instalada, pero no la estas usando.
- Has metido documentación en el código, pero no es una documentación adecuada ejemplo:
    ```def insert_price(db: Session, symbol: str, price: float, date: str) -> None:
        """
        Inserts or updates the price of an asset in the database.
        """
  ```
    Como debería ser:
    ```
   def identify(file: UploadFile, user_id: str, request: Request) -> list[dict]:
    """Identify the bottle cap of an image.

    Args:
    ----
        file: The file we are going to identify in an image.
        user_id: The user_id of the person.
        request (Request): Needed for the limiter

    Returns:
    -------
        The result of the identification of the bottle cap in a dictionary.
    """
  ```
  Es decir cada definición deberia tener una explicación de la función y de cada parámetro, además de lo que responde.
- [No uses `Optional[float]` usa `float | None`](https://github.com/RafaelRemoteDev/CotizAPI/blob/main/managers/assets_manager.py#L69C63-L69C78) esto viene por defecto a partir de Python 3.10
- [No uses variables hardcodeadas](https://github.com/RafaelRemoteDev/CotizAPI/blob/main/services/yahoo_finance.py#L9), `return datetime.now().weekday() >= 5` en su lugar deberías crear una variable: `WEEK_DAY: int = 5` y usarla.
- Lo mismo con `results: Dict[str, Optional[float]] = {}` en su lugar pon: `:dict[str, float | None]`, esto para el resto del código.

Por lo demás todo bien, sigue así :) Muy buen avance en estos últimos dias.