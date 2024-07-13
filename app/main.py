from datetime import datetime

from pydantic import BaseModel
from abc import ABC, abstractmethod


class User(BaseModel, ABC):
    id: int
    name: str = 'Pepito de los palotes'

    @abstractmethod
    def es_admin(self):
        ...


class Admin(User):
    date_start: datetime = datetime.now()

    def es_admin(self):
        print(f"El usuario {self.name} es admin y empezo a ser administrador en la fecha de {self.date_start}")


class NormalUser(User):
    def es_admin(self):
        print(f"El usuario con {self.id} ha intentado acceder al metodo es_admin")


if __name__ == '__main__':
    a = Admin(id=2, name="Paco")
    a.es_admin()

    b = NormalUser(id=3, name="Pepe")
    b.es_admin()
