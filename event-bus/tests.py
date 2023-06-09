import unittest
from event_bus import EventBus, Listener, Source


def test_handler(v):
    return v


class TestListener(unittest.TestCase):

    def test_adds_actions(self):
        listener = Listener('test')
        self.assertEqual(len(listener.actions), 0)
        listener.add_action(test_handler)
        self.assertEqual(len(listener.actions), 1)

    def test_remove_actions(self):
        listener = Listener('test')
        self.assertEqual(len(listener.actions), 0)
        listener.add_action(test_handler)
        self.assertEqual(len(listener.actions), 1)
        listener.remove_action(test_handler)
        self.assertEqual(len(listener.actions), 0)


class TestEventBus(unittest.TestCase):

    def test_adds_actions(self):
        bus = EventBus()
        listener = Listener('test')

        self.assertEqual(len(bus.listeners), 0)
        listener.connect(bus)
        self.assertEqual(len(bus.listeners), 1)


if __name__ == "__main__":
    unittest.main()
