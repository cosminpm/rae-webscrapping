"""
Given two strings s and t, return true if t is an
anagram of s, and false otherwise.
"""


# Las letras tienen que ser la mismas, da igual el orden


# rat != car
# car == arc
# rac == arc

# Contar el numero de lentras y que el numero de letras sea el mismo
# "a" -> X
# "B" -> Y

# {"a" : X}
# key/llave/palabra : value/valor/definicion
# str : int, float, str, listas, dictionary, sets, class

# funcion que la transform la entrada en un hash

# O(1)
# sets

# listas
# O(n)

# 27 letras -> 27 manos

def is_anagram(p1: str, p2: str) -> bool:
    # Longitud distinta
    if len(p1) != len(p2): return False
    cuerpo = dict()

    # = asignaciones
    for l1 in p1:
        if l1 not in cuerpo:
            cuerpo[l1] = 0
        cuerpo[l1] += 1

    for l2 in p2:
        if l2 not in cuerpo:
            return False
        if cuerpo[l2] == 0:
            return False
        cuerpo[l2] -= 1
    return True


if __name__ == '__main__':
    palabra1 = "cara"
    palabra2 = "arca"

    palabra1 = "anagram"
    palabra2 = "nagaram"

    palabra1 = "car"
    palabra2 = "rat"

    res = is_anagram(palabra1, palabra2)
    print(res)