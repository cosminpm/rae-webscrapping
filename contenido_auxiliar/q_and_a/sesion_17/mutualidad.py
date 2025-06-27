def main():
    bienvenida: str = "hola soy cosmin"
    edad: int = 12
    peso: float = 70.5

    # La linea 7 y 8 son exactamente lo mismo
    loteria = (5, 6, 8, 10)
    loteria: tuple = (5, 6, 8, 10)

    loteria: list = (5, 6, 8, 10)  # Esto no falla, pero el IDE (PyCharm) te da un warning

    loteria: list = [5, 6, 8, 10]

    # loteria = tuple(5, 6, 8, 10) # NO CORRECTO
    loteria = tuple([5, 6, 7, 8])
    # [5, 6, 7, 8]    <- lista
    # tuple(), list() <- conversion

    no_soy_chino: bool = False
    soy_chino: bool = True

    # if soy_chino:
    #     print("De verdad que soy chino")

    # verdadery = [1]
    # if verdadery:
    #     print("DE VERDAD")

    verdadery = 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
    if not verdadery:
        print("SOY COSMIN EL PEOR PROFESOR DEL MUNDO")

    # 0, 1, 2, 3, 5
    matricula = [4, 0, 7, 0, "MSC", [1, 2, 3], ]
    matricula[4] = 4070.12345

    tengo_la_mano_levantado = False
    tengo_la_mano_levantado = True
    tengo_la_mano_levantado = 1234
    tengo_la_mano_levantado = (1, 2, 3, 4)
    # tengo_la_mano_levantado = 1234567.89123
    tengo_la_mano_levantado = 2

    print(tengo_la_mano_levantado)

    # loteria: tuple = (5, 6, 8, 10)
    # loteria[0] = 5555


if __name__ == '__main__':
    main()
