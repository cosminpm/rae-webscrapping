from datetime import datetime


class Persona:
    def __init__(self, edad: int, nombre: str):
        self.edad = edad
        self.nombre = nombre

    def imprimir_informacion(self):
        print(f"Tengo {self.edad} anios y mi nombre es {self.nombre}")


def main():
    # Tipos de Datos Simples
    # string, int, float, bool

    # Tipos de Datos Complejos
    # tuple, list, dict, set

    # tuple vs list -> tupla es inmutable
    # tuple: ()

    # list vs set (conjunto) ->

    lista: list = ["a", "b", "c", "z", "d"]
    conjunto: set = {"a", "b", "c", "z", "d"}

    # print(conjunto[0])
    print(lista, conjunto)

    # buscar en la lista, la "d"

    for character in lista:
        if character == "d":
            print("He encontrado la d.")

    esta_en_conjunto: bool = "d" in conjunto
    print(esta_en_conjunto, "esta en conjunto")

    cadena: str = "Hola"
    print(cadena[0])

    dt = datetime(2025, 5, 2)
    print(dt.weekday())

    cosmin = Persona(24, "Cosmin")
    cosmin.imprimir_informacion()


if __name__ == '__main__':
    main()
