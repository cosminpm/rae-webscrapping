def main():
    # si no tiene un : es un set
    canicas = {"verde", "roja", "azul", 1, 2, 3, 123.123, "rosa", (1, 2, 3)}
    # funciona con todos los tipos simples y las tuplas
    print(type(canicas))

    # si tiene : es una dict
    diccionario = {"verde": "el color verde es el del bosque", 1: "Esto es el numero 1", "uno": 1}
    print(type(diccionario))

    bolsa_de_canicas_museo = ("verde", "roja")
    bolsa_de_canicas_parque = ["verde", "roja"]

    # (),    [],    {}
    # tupla, lista, set


if __name__ == '__main__':
    main()
