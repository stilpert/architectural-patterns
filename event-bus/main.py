from event_bus import EventBus, EventListener, EventSource


def handle_big(sound):
    print(f'HANDLE {sound.upper()}')


def handle_small(sound):
    print(f'handle {sound.lower()}')


if __name__ == '__main__':
    bus = EventBus()

    cat_listener = EventListener('cat')
    dog_listener = EventListener('dog')

    cat_listener.connect(bus)
    dog_listener.connect(bus)

    cat_listener.add_action(handle_big)
    cat_listener.add_action(handle_small)

    cat_source = EventSource('cat', bus)
    #
    cat_source.emit('meow')
    cat_source.emit('purr')
