# list (llamada a su metodo copy) -> va al primer elemento y mira lo que es si tiene copy llama a su copy
def cambios(mi_objeto: list):
    mi_objeto[1] = {1, "b", "c"}


def cambios_2(mi_objeto: list):
    mi_objeto[1][2] = {1, "b", "c"}


def main():
    mi_objeto = [{"a": "soy a", "b": "soy b"}, {1: "soy un uno", 2: [1, 2, 3, 4, 5, 6]}]
    cambios_2(mi_objeto.copy())
    print(mi_objeto)


if __name__ == '__main__':
    main()
