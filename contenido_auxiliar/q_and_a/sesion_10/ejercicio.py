"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""


# CUAL NUMERO FALTA
# PUDE SER QUE NO FALTE NINGUNO
# SI NO FALTA FALTA SIGUIENTE


def solucion_matematica():
    nums = [3, 0, 1, 2]
    # nums = [3, 0, 1]    -> Falta el 2
    # nums = [0, 1, 2, 3] -> Falta el 4
    # Siempre faltara un numero

    # Obtenemos la longitud del array o el numero de elementos -> n
    n_elementos = len(nums)
    # Calculamos el sumatorio hasta n + 1
    expected = (n_elementos * (n_elementos + 1)) // 2

    # La resta de lo esperado y lo que hay
    res = expected - sum(nums)

    # Si el array es un array completo, nos dara el siguiente numero

    # Si no esta completo nos dara el numero que falta

    # creo es el sumatorio de 0 ... n + 1 (n_elementos * (n_elementos + 1)) // 2 -
    return res

    #


def solucion_informatica():
    nums = [3, 0, 1]
    # nums = [3, 0, 1]    -> Falta el 2

    # nums = [0, 1, 2, 3] -> Falta el 4

    nums = sorted(nums)
    # nums = [0, 1, 2, 3]
    # nums = [0, 1, 2, 3, 4]

    for i in range(1, len(nums)):
        anterior: int = i - 1
        if nums[i] - 1 != nums[anterior]:
            return nums[anterior] + 1
    return nums[len(nums) - 1] + 1


if __name__ == '__main__':
    res = solucion_informatica()
    print(res)