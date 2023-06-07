import random


class Blackboard(object):
    max_capacity = 10

    def __init__(self):
        self.cars = []
        self.car_data = []
        self.progress = 0

    def add_car(self, car):
        self.cars.append(car)

    def add_data(self, data):
        print('adding data', self.progress)
        self.car_data.append(data)
        self.progress += 1

    def is_polling(self):
        return self.progress < self.max_capacity


class Controller(object):

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def run(self):
        while self.blackboard.is_polling():
            for car in self.blackboard.cars:
                if car.is_photographed:
                    car.share_data()
        return self.blackboard.car_data


class Car:
    avg_speed = 60
    type = 'unknown'

    def __init__(self, blackboard):
        self.blackboard = blackboard

    def is_photographed(self):
        return False

    def get_speed(self):
        return self.avg_speed + random.randint(-1, 1) * 10

    def share_data(self):
        self.blackboard.add_data(
            {"type": self.type, "speed": self.get_speed()})


class Truck(Car):
    type = 'Truck'
    avg_speed = 40

    def is_photographed(self):
        return random.randint(0, 1) * random.randint(0, 1)


class Sedan(Car):
    type = 'Sedan'
    avg_speed = 60

    def is_photographed(self):
        return True


class Suv(Car):
    type = 'SUV'
    avg_speed = 70

    def is_photographed(self):
        return random.randint(0, 1)
