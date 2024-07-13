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

## Enlaces de interes

- [Libreria de pydantic](https://docs.pydantic.dev/latest/concepts/models/) : Contiene informacion sobre como construir
  clases.

## Ejercicio para clases de POO


### Ejercicio 1

Crear una clase Abstracta que sea Word/Palabra que contenga  los campos necesarios para una entrada de la RAE.
  - palabra
  - definicion
  - enlace
  - tipo

### Ejercicio 2

Crear distintas clases de palabras tales como Verbo y Sustantivo, haciendo un metodo de validacion para detectar si es un verbo en infinitivo u otra cosa, este metodo abstracto tiene que estar definido en la clase abstracta e implementado en las otras subclases.

### Ejercicio 3

Usar el operador Walrus en alguno de los ifs implementados.


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