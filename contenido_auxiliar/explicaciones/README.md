
# Respuestas a dudas generales

1. En el archivo main, entiendo que “fastapi” es un framework que se usa para crear API. Y entonces, ¿qué es “FastAPI” (en mayúsculas), que la/lo importas de “fastapi” (en minúsculas)?
    
    - ```python
      from fastapi import FastAPI
      app = FastAPI()
      ```
    - `fastapi` es **TODO** el framework
    - `FastAPI` es el inicializador de la API, de nuestra app
    - [fastapi documentation](https://github.com/fastapi/fastapi)
2. ¿Qué es uvicorn y para qué la/lo importas?
    - ``` python
      import uvicorn
      uvicorn.run(app, host="127.0.0.1", port=8000)
      ```
    - Vercel para deployar APIs para todo el mundo de forma gratuita.
    - AWS es de pago pero tiene una capa gratuita.
    - [uvicorn](https://www.uvicorn.org/)
    - [asgi](https://asgi.readthedocs.io/en/latest/)

3. ¿Qué significa “app = FastAPI()”? ¿Qué es esta variable “app” que creaste y a la que le asignas el valor “FastAPI()”? ¿Para qué sirve? ¿Por qué la necesitamos para crear una API?
   - Estamos construyendo el esqueleto de la app.


4. ¿Qué significa esta línea `uvicorn.run(app, host=’127.0.0.1’, port=8000)`? ¿Es un método que se llama `uvicorn.run`? Si es así, ¿qué hace? ¿Por qué necesita esos parámetros y qué son esos parámetros exactamente? ¿Qué son exactamente los parámetros “host” y “port”? ¿Da lo mismo asignarles esos valores que otros? ¿O hay una razón para que le asignes esos valores específicos? Sin importar dónde me encuentre yo geográficamente, ¿usaré esos mismos valores para los parámetros de host y port?
   - Significa `uvicorn.run(app, host=’127.0.0.1’, port=8000)` poner nuestra app a la red.
5. En el contexto de los métodos HTTP, dices que “get” sirve para obtener recursos. ¿Qué son recursos?
   - Recursos es cualquier tipo de informacion.
   - json

6. Escribes el siguiente fragmento de código:
   ```
   @app.get(“/”)
   def root():
     return “Hola, mundo”
   ```
   ¿Puedes, por favor, explicar línea por línea lo que estás haciendo aquí?
   el signo “@” (que usaste en clases anteriores para crear “decoradores”)
   
   Me atrevo a pensar, por clases anteriores, que estás “wrapping” esta función/método “root” con el decorador “@app.get(“/”)”, pero solo lo sospecho y, en todo caso, no entiendo por qué ni para qué lo haces. Más importante aún, ¿qué pasaría si no lo envolvieras (¿o encapsularas?) con ese decorador? Naturalmente, esto último tiene sentido solo si, en efecto, “@app.get(“/”)” es un decorador.
   Y ya que, en general, “get” sirve para obtener recursos, ¿qué recursos estás obteniendo con este “get”?

   - Un recurso es cualquier tipo de cadena o imagen o cualquier cosa que devuelva nuestra API, en este caso una cadena.

7. Dices que “en un API podemos tener distintos tipos de ‘endpoints”. (timestamp del video: -18:40). ¿Qué es “endpoint” y cómo se relaciona con el comando “get” que usaste?  Además, dices que ese “get” (el de mi pregunta 6) simplemente sirve para pasar un parámetro (en nuestro caso, ¿cuál parámetro estamos pasando?) y obtener algo a cambio (¿qué estamos obteniendo en nuestro caso?), o incluso sin pasar ningún parámetro: es simplemente una devolución de información (en este caso, ¿qué información nos están devolviendo?)
   - Son los puntos de comunicacion que nos da la API, las funciones que nos permite ejecutar.
   - Un parametro son las variables que se pasan

8. Dices que el “post” sirve para crear un recurso nuevo y también para obtener recursos con parámetros más complejos. ¿Qué son recursos? Ya te lo pregunté en mi pregunta 5, pero lo repito por si acaso, para que no se nos pase por alto
   - Resuelta en el ejecicio anterior

9. Pusiste un segundo ejemplo de “get”, pero no entiendo qué añade o qué aclara respecto al primer “get” (el de mi pregunta 5):
   ```python
   @app.get(“/dime_hola_caracola”)
   def root():
     return “Hola, caracola”
   ```

10. ¿Qué es un archivo “router”? ¿Por qué se llama así, como “route” o “ruta”? ¿Y por qué lo necesitamos? ¿Para qué sirve?
    - Sirve para subdividir y no hacer complejo el fichero principal.
11. En el archivo “router_rae.py” que creaste, ¿qué es “APIRouter”, que también la/lo importas de “fastapi”?
    - Se ha resuelto en las anteriores. 
