import unittest
from layers import ApplicationLayer, DataLayer, PresentationLayer


class TestDataLayer(unittest.TestCase):
    def setUp(self):
        self.dataLayer = DataLayer()

    def test_loads_db(self):
        self.assertGreater(len(self.dataLayer.persons), 0)

    def test_returns_names(self):
        self.assertGreater(len(self.dataLayer.get_persons_names()), 0)

    def test_returns_ages(self):
        self.assertNotEqual(self.dataLayer.get_person_age(self.dataLayer.get_persons_names()[0]), None)

    def test_returns_none_ages(self):
        self.assertEqual(self.dataLayer.get_person_age('---'), None)
        self.assertEqual(self.dataLayer.get_person_age(''), None)
        self.assertEqual(self.dataLayer.get_person_age(None), None)


class TestApplicationLayer(unittest.TestCase):
    def setUp(self):
        self.app_layer = ApplicationLayer(DataLayer())

    def test_loads_cache(self):
        self.assertEqual(self.app_layer.is_init, False)
        self.assertEqual(self.app_layer.names_cache, None)

        self.app_layer.get_person_age('')

        self.assertEqual(self.app_layer.is_init, True)
        self.assertGreater(len(self.app_layer.names_cache), 0)

    def test_returns_ages(self):
        self.app_layer.get_person_age('')

        self.assertNotEqual(self.app_layer.get_person_age(self.app_layer.names_cache[0]), None)

    def test_returns_none_ages(self):
        self.assertEqual(self.app_layer.get_person_age(''), None)


if __name__ == "__main__":
    unittest.main()
