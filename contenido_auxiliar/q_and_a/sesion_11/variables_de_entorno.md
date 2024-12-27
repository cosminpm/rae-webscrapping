# Problema


El problema es que tenemos diferentes configuraciones para remoto y local.

#### _Esto esta mal_
```python
# host = "192.0.0.1"
host = "192.0.0.2"
```

#### Solucion
Usando variables de entorno.

La forma rápida y sencilla es poner el HOST en tu env y luego hacerÑ

```.env
HOST=0.0.0.0
PORT=8000
```

- [Definir variables de entorno en Vercel](https://vercel.com/docs/projects/environment-variables)

```python
import os
host: str = os.getenv("HOST")
port: str = os.getenv("PORT")
```

#### La mejor forma

Usar un fichero de config.py que lea las variables de entorno automáticamente después de hacer un `load_dotenv()`
Ejemplo: [enlace](https://github.com/cosminpm/bottle-caps-backend/blob/main/app/config.py)

```python
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

LIMIT_PERIOD: str = "15/minute"


class Settings(BaseSettings):
    firebase_config_file: str
    firebase_bucket: str

    pinecone_api_key: str
    pinecone_env: str

    profiling_time: bool = False

    save_image: bool = False
    host: str = "0.0.0.0"  # noqa: S104
    port: int = 8080
    prefix_url: str = "http://"
    torch_home: str = "./model"

    api_key: str = "dumb_key"

# Algo asi
from <BLABLA> import Settings
settings = Settings()

settings.host


```
[Enlace documentación oficial](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage)