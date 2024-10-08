# RAE webscrapping

## Tipos de ficheros

### .gitignore

Eliminar los ficheros de PyCharm: `git rm -rf --cached .idea/`

Es un fichero para ignorar directorios/ficheros que no queremos que se suban a la nube _(en este caso GitHub)._

### requirements.txt

Es un fichero que librerias hacen falta para correr un determinado programa.

## Comandos de git

- `git add <FICHERO>` para aniadir ficheros de interes en local
- `git commit -m <MENSAJE>` para aniadir los cambios a la rama local
- `git push` para enviar los cambios al remoto

## Comandos de bash
- `pip`: Manjeador de librerias de Python
  - `freeze`: Nos indica los paquetes que tenemos en nuestro virtual environment.


## Enlaces de interes

- [Libreria de pydantic](https://docs.pydantic.dev/latest/concepts/models/) : Contiene informacion sobre como construir
  clases.
- [User Angents](https://user-agents.net/): Para obtener agentes de usuario que nos permitan autorizarnos en algunas páginas web.
- [Tipos de respuesta de HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Status): Codigos y sus descripciones al realizar una solicitud HTTP.
## Estructura de un proyecto

- Siempre habra una carpeta llamada `app` con el código.
- Luego tendremos `schemas` que servira para definir las clases de "pydantic".
- Luego tendremos `infraestructure` que servira para tener los modelos de las bases de datos.
- Luego tendremos los `services` el codigo que usa las clases definidas con antelacion.

## Descripcion del proyecto

Bot de telegram que dado un comando y una palabra busque esa palabra en la RAE.

La palabra se descargara en la base de datos local la primera vez que se haga la consulta. Si se vuelve a pedir dicha palabra se obtendra automaticamente de la base de datos.

El proyecto consistira en crear:

- Un backend en Python que nos sirva como API.
  - Un webscrappeer en este backend que nos permita obtener las definiciones de la RAE.
  - La estructura del proyecto estara definida con clases y programacion orientada a objetos.
  - Las librerias principales que se utilizaran seran `re`,`fastapi`,`pydantic`,`bs4`.
- Tener una base de datos local con SQLite.
- Usar PostMan para probar la API.
- Tener el repositorio en GitHub para poder enseniarlo.
- Aprender a usar el debugger con PyCharm.
- Aprender a conectar Telegram a nustra API.