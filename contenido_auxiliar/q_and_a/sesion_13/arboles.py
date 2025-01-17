# hojas
# ramas
# nodos
from pydantic import BaseModel


# Un nodo sin hijos se llama nodo hoja.

class Nodo:
    def __int__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def is_leaf(self):
        return len(self.children) == 0


# Deberes
# Implementar el metodo que desacopla es decir: que deja de tener la rama, en el nodo que hayamos dicho. Usar la motosierra.
# Implementar el metodo de visualizacion de un arbol.


if __name__ == '__main__':
    ...
