class Source:
    def __init__(self, event, bus=None) -> None:
        self.bus = bus
        self.event = event

    def emit(self, value):
        self.bus.emit(self.event, value)

    def connect(self, bus):
        self.bus = bus


class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event, listener):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(listener)

    def emit(self, event, value):
        if event not in self.listeners:
            return

        for listener in self.listeners[event]:
            listener.invoke(value)


class Listener:
    def __init__(self, event) -> None:
        self.bus = None
        self.actions = []
        self.event = event

    def connect(self, bus):
        self.bus = bus
        self.bus.subscribe(self.event, self)

    def add_action(self, action):
        self.actions.append(action)

    def remove_action(self, action):
        self.actions.remove(action)

    def invoke(self, value):
        for action in self.actions:
            action(value)


def handle_first_type(sound):
    print(f'HANDLE FIRST UPPER {sound.upper()}')


def handle_second_type(sound):
    print(f'handle second lower {sound.lower()}')


if __name__ == '__main__':
    bus = EventBus()

    first_listener = Listener('first listener')
    second_listener = Listener('second listener')

    first_listener.connect(bus)
    second_listener.connect(bus)

    first_listener.add_action(handle_first_type)
    first_listener.add_action(handle_second_type)

    first_source = Source('first', bus)
    #
    first_source.emit('first works!')
    first_source.emit('second works!')
