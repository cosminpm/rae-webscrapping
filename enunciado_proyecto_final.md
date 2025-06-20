# Plantilla del Proyecto de Examen Final

Este proyecto tiene como objetivo desarrollar un sistema similar al de la Real Academia Española (RAE), pero con una temática diferente a elección del estudiante. A continuación, se detallan los requisitos y directrices para completar exitosamente el proyecto de examen final.

## Requisitos Mínimos

### 1. *Desarrollo de la API*
- *Framework*: Utiliza el framework de tu preferencia (por ejemplo, FastAPI, Flask, Django).
  
### 2. *Base de Datos*
- *Recomendación*: Utiliza SQLite.
- *Scripts de Creación*: Incluye scripts para la creación de la base de datos.

### 3. *Organización del Proyecto*
- *Estructura*: Organiza el proyecto siguiendo la estructura de Manager y Routers vista en clase.
- *Patrón de Diseño*: Implementa el patrón UnitOfWork.
- *Librerías*: Utiliza Pydantic y SQLAlchemy para la organización de ficheros.

### 4. *Control de Versiones*
- *Repositorio*: Sube el proyecto a GitHub.
- *README*: Incluye un archivo README detallado que explique todo el proyecto.

### 5. *Pruebas*
- *Tests Unitarios*: Implementa pruebas unitarias.
- *Tests de Integración*: Implementa pruebas de integración.

### 6. *Frontend*
- *Conexión*: Conecta el proyecto a un frontend sencillo. Puedes utilizar Telegram como se explicó en clase.

### 7. *Consumo de Datos*
- *Fuente de Datos*: El proyecto debe consumir datos de una fuente externa, ya sea mediante web scraping de una página web o utilizando una API disponible (por ejemplo, APIs de fútbol con capas gratuitas).

### 8. *Endpoints de Postman*
- *Ejemplos*: Proporciona los endpoints listos para usar en un ejemplo mediante Postman.

### 9. *Documentación de Problemas*
- *Readme*: Explica tres problemas que hayas resuelto utilizando el depurador integrado de PyCharm.
- *Capturas*: Incluye capturas de pantalla que muestren cómo utilizaste el depurador.

### 10. *Modelo de Datos*
- *Relaciones*: La base de datos debe tener al menos dos tablas relacionadas (por ejemplo, camisas y botones).

### 11. *Funciones*
- *Funciones*: Usar Walrus Operator.
- *Comprensión de listas*: Usar comprensión de listas tal y como hemos visto en clase.

### 12. *Logging*
- *Loguru*: Usar loguru para imprimir por pantalla las partes importantes del proyecto.

## Puntos Extra (Opcionales)

Estos elementos no se han explicado directamente, pero pueden aportar valor adicional al proyecto y se necesitará un mínimo de 3 puntos opcionales para presentar el proyecto.

### 1. *Frontend Alternativo*
- *Opciones*: Utiliza un frontend diferente a Telegram, como un HTML sencillo que apunte a nuestro backend o Discord.

### 2. *Despliegue*
- *Hosting*: Despliega el proyecto en Vercel o cualquier otro servidor gratuito o de pago.
- *Valor*: Este punto cuenta por 3 puntos adicionales, ya que es muy valorado para oportunidades laborales.

### 3. *Autenticación*
- *Implementación*: Añade un sistema de autenticación al proyecto. Puedes utilizar Bearer Token como referencia.

### 4. *Uso de Firebase*
- *Opciones*: Utiliza Firebase como base de datos o para añadir más funcionalidades.
- *Valor*: Este punto cuenta por 2 puntos adicionales.
- *Documentacion*: https://firebase.google.com/docs/reference/admin/python

### 5. *Modelo de Datos Avanzado*
- *Relaciones*: Amplía la base de datos para que tenga al menos cinco tablas relacionadas entre sí.

### 6. *Scripting*
- *Scripts*: Crear un fichero .sh o .bat o un Makefile dependiendo del sistema que tengáis para desplegar o ejecutar algunos de vuestros scripts.

### 7. *Contendores*
- *Docker*: Usar docker para vuestro proyecto.
- *Valor*: Este punto cuenta por 2 puntos adicionales.

### 8. *Debugger*
- *Avanzado*: Usar debugger con un if condicional.

### 9. *versionado de versiones de base de datos* 
- *Alembic*: Hacer cambios en la base de datos y usar Alembic para las distintas versiones
- *Valor*: Este punto cuenta por 3 puntos adicionales.

### 10. *Observabilidad*
- *Sentry*: Aplicar Sentry al proyecto.

### 11. *Profiling*
- *Velocidad*: Aplicar alguna lirberia como pyinstrument al proyecto para ver que metodos usan mas tiempo en el proyecto.

### 12. *Bases de datos*
- *BBDD*: Montar otra base de datos que no sea SQLlite, tal como MariaDB
- *Valor*: Este punto cuenta por 2 puntos adicionales.


## Presentación Final

Una vez finalizado el proyecto, se realizará una presentación (showcase) frente a los demás alumnos y el profesor. Durante la presentación, el profesor podrá hacer preguntas sobre el proyecto e incluso solicitar modificaciones en directo, preguntando cómo implementarían ciertas funcionalidades o cómo resolvieron determinados aspectos del proyecto.

## Recursos Adicionales

- **Documentación de [FastAPI](https://fastapi.tiangolo.com/)**
- **Documentación de [Flask](https://flask.palletsprojects.com/)**
- **Documentación de [Django](https://www.djangoproject.com/)**
- **Guía de [SQLAlchemy](https://www.sqlalchemy.org/)**
- **Introducción a [Pydantic](https://pydantic-docs.helpmanual.io/)**
- *Uso de [Postman](https://www.postman.com/) para probar APIs*

## Contacto

Para cualquier duda o consulta, por favor contacta con el profesor o los asistentes del curso.

---

¡Buena suerte con tu proyecto!
