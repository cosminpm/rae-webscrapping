# El error consta de que j tiene que ser igual a 1 y no a i

def main():
    dibujo = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0]
    ]

    for fila in dibujo:
        for columna in fila:
            if columna == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


if __name__ == '__main__':
    main()
