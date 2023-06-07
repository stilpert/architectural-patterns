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


class EventSource:
    def __init__(self, event, bus=None) -> None:
        self.bus = bus
        self.event = event

    def emit(self, value):
        self.bus.emit(self.event, value)

    def connect(self, bus):
        self.bus = bus


class EventListener:
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
