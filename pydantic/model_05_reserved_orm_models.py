""" usage model 05 reserved orm models
ORM 인스턴스는 최상위 수준뿐만 아니라 from_orm으로 반복적으로 구문 분석됩니다.
여기서 바닐라 클래스는 원리를 증명하기 위해 사용되지만, 대신 모든 ORM 클래스가 사용될 수 있다.
"""
from typing import List

from pydantic import BaseModel


class PetCls:

    def __init__(self, *, name: str, species: str):
        self.name = name
        self.species = species


class PersonCls:

    def __init__(self, *, name: str, age: float=None, pets: List[PetCls]):
        self.name = name
        self.age = age
        self.pets = pets


class Pet(BaseModel):
    name: str
    species: str

    class Config:
        orm_mode = True


class Person(BaseModel):
    name: str
    age: float = None
    pets: List[Pet]

    class Config:
        orm_mode = True


if __name__ == '__main__':
    bones = PetCls(name='Bones', species='dog')
    orion = PetCls(name='Orion', species='cat')

    anna = PersonCls(name='Anna', age=20, pets=[bones, orion])
    anna_model = Person.from_orm(anna)
    print(anna_model)
