# pip install NOMBRE_DEL_PAQUETE
# pip install requests
# https://www.freecodecamp.org/espanol/news/python-if-name-main/
# Ctrl + Alt + Shift + Mayusculas + Clicks en lineas

# Importar libreria
import requests

def paco_y_manolo():
    dibujo = [[0, 0, 0, 1, 0, 0, 0],
              [0, 0, 1, 1, 1, 0, 0],
              [0, 0, 1, 1, 1, 1, 0],
              [0, 1, 1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 1, 0, 0, 0]]

    # i = 1 -> [0, 0, 0, 1, 0, 0, 0]
    # i = 2 -> [0, 0, 1, 1, 1, 0, 0]
    # j = 1 -> [0, 0, 0, 1, 0, 0, 0]
    # i = 0, j = 3 (0, 1)

    for i in dibujo:
        for j in i:
            if j == 1:
                print("👀", end="")
            else:
                print(" ", end="")
        print("\n")


def mi_bar():
    paco_y_manolo()


if __name__ == '__main__':
    paco_y_manolo()
