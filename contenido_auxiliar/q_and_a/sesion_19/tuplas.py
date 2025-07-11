# pip install loguru

from loguru import logger


def tuplas():
    bono_loteria = (1, 6, 3, 0, 2)
    print(type(bono_loteria))

    # Tupla                  ()
    # Lista                  []
    # Diccionario            {:}
    # Set/Conjunto           {}

    # diccionario
    rae = {
        "patata": "una verdura"
    }

    print(rae["patata"])


def conjuntos():
    # saber si goku esta en el set es O(1)
    # figuritas: set = {"power ranger rojo", "goku", "yoda", "yoda", "yoda", 1, 1.2, "yoda1"}
    # logger.info(figuritas)

    # n es el tamanio de la lista, saber si goku esta en la lista es O(n)
    figuritas: list = ["power ranger rojo", "yoda", "yoda", "yoda", 1, 1.2, "yoda1", "goku"]
    logger.info(figuritas)

    logger.info(figuritas[1])
    # logger.info(figuritas["yoda"])
    # O(n) O(1)


    # logger.error(figuritas)
    # logger.warning(figuritas)
    # logger.debug(figuritas)


if __name__ == '__main__':
    conjuntos()
