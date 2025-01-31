# class Nodo:
#     def __int__(self, data):
#         self.data = data
#         self.children = []
#
#     def add_child(self, child):
#         self.children.append(child)
#
#     def is_leaf(self):
#         return len(self.children) == 0

from pydantic import BaseModel


# class Node(BaseModel):

class Perro:
    def __init__(self, color: str, piernas: int = 4):  # Para inicializar el objeto
        self.color = color
        self.piernas = piernas
        self.edad = 0

    def envejecer(self):
        self.edad += 1

    @staticmethod
    def ladrar():
        print("Guau")


class OppType(BaseModel):
    sql_query: str


# clientes
# campanias
# oportunidades -> incrementar el gasto en campania

# opp_type -> aumentar la visibilidad -> opp_type y campain = opportunidad
# opp_type -> aumentar el tiempo


class Opp(BaseModel):
    opp_id: int
    last_updated: float
    opp_type: OppType


def pelea_de_perros(p1: Perro, p2: Perro):
    ...


def main():
    perro_1 = Perro("negro")
    perro_2 = Perro("marron", 3)

    perro_1.envejecer()
    print(perro_1.color, perro_1.piernas, perro_1.edad)
    perro_1.ladrar()


if __name__ == '__main__':
    main()
