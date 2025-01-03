# # Enunciado
#
# Dado una lista de listas que representan una imagen en blanco (0) y negro (1), invierte la imagen.
#
# Ejemplo:
#
# ```python
# image =      [[0,0,1],[0,1,0],[1,1,1]] ->
# resultado = [[1,1,0],[1,0,1],[0,0,0]]  -> gallina
# ```

def invertir_imagen(image: list[list[int]]) -> list[list[int]]:
    # editar el input original
    # o hacer una copia e ir editando

    resultado = []

    for fila in image:
        temporal: list = []  # Primero creamos una lista temporal que se va sobrescribiendo en cada iteracion a vacia
        for color in fila:
            if color == 0:
                temporal.append(1)
            else:
                temporal.append(0)
        resultado.append(temporal)
    return resultado


def main():
    image = [[0, 0, 1], [0, 1, 0], [1, 1, 1]]
    res = invertir_imagen(image)
    print(res)

if __name__ == '__main__':
    main()
