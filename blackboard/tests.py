import unittest
from blackboard import Truck, Controller, Blackboard


def test_handler(v):
    return v


class TestBlackboard(unittest.TestCase):

    def test_is_polling(self):
        bb = Blackboard()
        self.assertEqual(bb.is_polling(), True)
        bb.progress = bb.max_capacity
        self.assertEqual(bb.is_polling(), False)

    def test_add_cat(self):
        bb = Blackboard()
        self.assertEqual(len(bb.cars), 0)
        bb.add_car(Truck(bb))
        self.assertEqual(len(bb.cars), 1)

    def test_add_car_data(self):
        bb = Blackboard()
        self.assertEqual(len(bb.car_data), 0)
        bb.add_data({})
        self.assertEqual(len(bb.car_data), 1)

    def test_invokes_cars(self):
        bb = Blackboard()
        bb.add_car(Truck(bb))

        self.assertEqual(len(bb.car_data), 0)
        bb.cars[0].share_data()
        self.assertEqual(len(bb.car_data), 1)


class TestCar(unittest.TestCase):

    def test_get_speed(self):

        car = Truck(None)
        self.assertNotEqual(car.get_speed(), car.get_speed())

    def test_is_photo(self):
        car = Truck(None)
        chunk = [car.is_photographed() for _ in range(0, 20)]
        self.assertNotEqual(all(chunk), True)


if __name__ == "__main__":
    unittest.main()
