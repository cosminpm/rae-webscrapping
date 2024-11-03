# Dado una cadena devolver True o False si es palindroma o no

# a
# " "
# aba
# abcd

# https://es.wikipedia.org/wiki/Orden_de_magnitud

def es_palindroma(cadena: str) -> bool:
    for i in range(0, len(cadena)):
        if cadena[i] != cadena[len(cadena) - 1 - i]:
            return False
    return True
    # Copia de n -> Orden de Magnitud O(n)
# n es nuetra entrada

# Tiempo O(n)
# Memoria O(1)
# Tiempo O(1)

# Tiempo O(n^2)
    # for fila in dibujo:
    #     for columna in fila:
    #         if columna == 1:
    #             print("*", end="")
    #         else:
    #             print(" ", end="")
    #     print()

# log n
# n * n2
# n log n

if __name__ == '__main__':
    entrada = "a"
    # entrada = ""
    # entrada = "aba"
    # entrada = "abcd"
    # entrada = "abccba"
    # a 0
    # b 1
    # c 2
    # d 3

    # 0 1 2 3 (4)
    res = es_palindroma(entrada)
    print(res)


# https://leetcode.com/
# https://neetcode.io/
# Mirar ordenes de  magnitud
