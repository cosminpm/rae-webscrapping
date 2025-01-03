# https://docs.python.org/3/library/copy.html

def por_referncia(diccionario: dict):
    diccionario["a"] = "hago una revolucion y quiero ser una b"


def main_diccionario():
    mi_diccionario = {"a": "soy una a"}
    por_referncia(mi_diccionario)
    print(mi_diccionario)


def referencia_lista(lista: list):
    lista[0] = 9999


def main_lista():
    mi_lista = [0, 1, 2, 3, 4, 5]
    referencia_lista(mi_lista.copy())
    print(mi_lista)


def copia(numero: str):
    numero = "pepito"


def main():
    mi_numero = "juanito"
    copia(mi_numero)
    print(mi_numero)


if __name__ == '__main__':
    main()
