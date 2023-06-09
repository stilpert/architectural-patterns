import random
from pprint import pprint


class Blackboard(object):
    max_capacity = 10

    def __init__(self):
        self.animals = []
        self.animal_data = []
        self.progress = 0

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_data(self, data):
        print('adding data', self.progress)
        self.animal_data.append(data)
        self.progress += 1

    def is_polling(self):
        return self.progress < self.max_capacity


class Controller(object):

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def run(self):
        while self.blackboard.is_polling():
            for animal in self.blackboard.animals:
                if animal.is_photographed:
                    animal.share_data()
        return self.blackboard.animal_data


class Animal:
    avg_weight = 60
    type = 'unknown'

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def is_photographed(self):
        return False

    def get_weight(self):
        return self.avg_weight + random.randint(-1, 1) * 10

    def share_data(self):
        self.blackboard.add_data(
            {"type": self.type, "weight": self.get_weight()})


class Horse(Animal):
    type = 'Horse'
    avg_weight = 40

    def is_photographed(self):
        return random.randint(0, 1) * random.randint(0, 1)


class Tiger(Animal):
    type = 'Tiger'
    avg_weight = 60

    def is_photographed(self):
        return True


class Lion(Animal):
    type = 'Lion'
    avg_weight = 70

    def is_photographed(self):
        return random.randint(0, 1)


if __name__ == '__main__':
    blackboard = Blackboard()

    blackboard.add_animal(Horse(blackboard))
    blackboard.add_animal(Lion(blackboard))
    blackboard.add_animal(Tiger(blackboard))

    res = Controller(blackboard).run()

    pprint(res)
