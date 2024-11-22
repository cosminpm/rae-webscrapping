# Given a string s consisting of words and spaces, return the length of the last word in the string.

# Casos de Prueba
# Ramon
# Juan Ramon
#
# Juan Ramon Perez del Castillo


def length_last_word(word: str) -> int:
    # contar las letras de la ultima
    # del final hasta el ultimo espacio
    # recorrer del reves

    # 0, 1, 2
    # a->0 b->1 c->2
    # abc -> 3
    #

    #                primer numero donde empieza
    #                segundo numero donde acaba
    #                tercer numero la direccion es dada por el simbolo (-/+), y el numero es el salto
    # for i in range(0, len(word), 1)

    # a  b  c
    # 0, 1, 2
    for i in range(len(word) - 1, -1, -1):
        print(word[i])


if __name__ == '__main__':
    case = "abc"
    length_last_word(case)
