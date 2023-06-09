import unittest
from models import NotificationModel
from controller import Controller


def test_handler(v):
    return v


class TestModel(unittest.TestCase):

    def test_adds_notification(self):
        model = NotificationModel()
        self.assertEqual(len(model.notifications), 0)
        model.add_notification('text 1')
        self.assertEqual(len(model.notifications), 1)


class TestController(unittest.TestCase):

    def test_adds_notification(self):
        controller = Controller(NotificationModel())
        self.assertEqual(len(controller.get_notifications_texts()), 0)
        controller.add_notification('text 1')
        self.assertEqual(len(controller.get_notifications_texts()), 1)


if __name__ == "__main__":
    unittest.main()
