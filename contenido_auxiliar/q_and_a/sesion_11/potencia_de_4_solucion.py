# # Given an integer n, return true if it is a power of four. Otherwise, return false.
# # An integer n is a power of four, if there exists an integer x such that n == 4x.
#
# Example 1:
#
# Input: n = 16
# Output: true
# Example 2:
#
# Input: n = 5
# Output: false
# Example 3:
#
# Input: n = 1
# Output: true

import math


def es_potencia_de_4(n: int) -> bool:
    if n == 1:
        return True
    elif n <= 0:
        return False
    res = math.log(n, 4)
    if res.is_integer():
        return True
    return False


if __name__ == '__main__':
    numero = 64
    resultado = es_potencia_de_4(numero)

    mensaje_bonito: str = f"El numero: {numero} es {resultado}"

    print(mensaje_bonito)
