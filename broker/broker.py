class Broker:
    def __init__(self):
        self.subscriptions = {}

    def subscribe(self, topic, handler):
        if topic not in self.subscriptions:
            self.subscriptions[topic] = []
        self.subscriptions[topic].append(handler)

    def unsubscribe(self, topic, handler):
        if topic in self.subscriptions:
            handlers = self.subscriptions[topic]
            if handler in handlers:
                handlers.remove(handler)

    def publish(self, topic, data):
        if topic in self.subscriptions:
            handlers = self.subscriptions[topic]
            for handler in handlers:
                handler(data)