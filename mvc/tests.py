import unittest
from models import AnimalModel
from controller import Controller


def test_handler(v):
    return v


class TestModel(unittest.TestCase):

    def test_adds_animal(self):
        model = AnimalModel()
        self.assertEqual(len(model.animals), 0)
        model.add_animal('name 1')
        self.assertEqual(len(model.animals), 1)


class TestController(unittest.TestCase):

    def test_adds_animal(self):
        controller = Controller(AnimalModel())
        self.assertEqual(len(controller.get_animals_names()), 0)
        controller.add_animal('name 1')
        self.assertEqual(len(controller.get_animals_names()), 1)


if __name__ == "__main__":
    unittest.main()
