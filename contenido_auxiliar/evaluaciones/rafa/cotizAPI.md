- (DB Browser for SQLite): Qué es esto?
- Faltan en el `README.md` como ejecutar el proyecto, esta solo la parte de instalación.
  - Un ejemplo de lo que falta, es que no has puesto como instalar las dependencias, es decir el: `pip install -r requirements.txt`
- El fichero `.env` no debe estar NUNCA publico.
- En el mismo repositorio, o por separado en un PDF, que me mandaras los puntos del enunciado que se han cumplido: [Enlace](https://github.com/cosminpm/rae-webscrapping/blob/master/Proyecto_final.md)
- La logica del `calcular_variaciones` debe estar fuera del routing, mirar estructura de rae_webscrapping.
- Es muy importante que uses SQLAlchemy para las conexiones a las base de datos, ya que ejecutar SQL queries, no es escalable a largo plazo y puede complicar mucho las cosas.
- El tipado de los argumentos tiene que estar en todas las funciones.
- En todas las funciones a no ser que sean funciones local que empiecen por _ tiene que haber documentacion.
- Pases todo al ingles, el codigo, lo que devuelve el bot o la api no tiene porque estar en ingles, pero el codigo si.