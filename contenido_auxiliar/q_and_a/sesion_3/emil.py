# def impar_mas_grande(*args):
#    res = 0
#   for numero in args:
#        if numero > res and numero % 2 == 1:
#            res = numero

#    return res
# if __name__ =='__main':
#    resultado = impar_mas_grande (*args:1, 9, 10, 0, 2, 3)
#    print(resultado)
# Primero el nivel de identacion estaba mal
# Segundo Has pasado los argumentos de forma erronea
# Tercero estabas imprimiendo la funcion, no el resultado

def impar_mas_grande(*args):
    print([i for i in args if i % 2 == 1])
    return max([i for i in args if i % 2 == 1])


if __name__ == '__main__':
    resultado = impar_mas_grande(1, 9, 10, 0, 2, 3)
    print(resultado)
