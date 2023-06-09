import unittest
from blackboard import Horse, Controller, Blackboard


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
        self.assertEqual(len(bb.animals), 0)
        bb.add_animal(Horse(bb))
        self.assertEqual(len(bb.animals), 1)

    def test_add_animal_data(self):
        bb = Blackboard()
        self.assertEqual(len(bb.animal_data), 0)
        bb.add_data({})
        self.assertEqual(len(bb.animal_data), 1)

    def test_invokes_animals(self):
        bb = Blackboard()
        bb.add_animal(Horse(bb))

        self.assertEqual(len(bb.animal_data), 0)
        bb.animals[0].share_data()
        self.assertEqual(len(bb.animal_data), 1)


class Testanimal(unittest.TestCase):

    def test_get_weight(self):

        animal = Horse(None)
        self.assertNotEqual(animal.get_weight(), animal.get_weight())

    def test_is_photo(self):
        animal = Horse(None)
        chunk = [animal.is_photographed() for _ in range(0, 20)]
        self.assertNotEqual(all(chunk), True)


if __name__ == "__main__":
    unittest.main()
