class Animal:
    def __init__(self, name) -> None:
        self.name = name


class AnimalModel:
    def __init__(self) -> None:
        self.animals = []

    def add_animal(self, name):
        self.animals.append(Animal(name))
