import pytest
from broker import *


@pytest.fixture
def broker():
    return Broker()

@pytest.fixture
def handler1():
    results = []
    def handler(data):
        results.append(f"Handler 1: {data}")
    return handler, results

@pytest.fixture
def handler2():
    results = []
    def handler(data):
        results.append(f"Handler 2: {data}")
    return handler, results


def test_pub_and_sub(broker, handler1, handler2):
    handler_func1, results1 = handler1
    handler_func2, results2 = handler2

    broker.subscribe("topic1", handler_func1)
    broker.subscribe("topic2", handler_func2)

    broker.publish("topic1", "topice 1 idk")
    broker.publish("topic2", "THREAD CANCELLED!!!!! ANT FARM GO")

    assert results1 == ["Handler 1: topice 1 idk"]
    assert results2 == ["Handler 2: THREAD CANCELLED!!!!! ANT FARM GO"]


def test_unsub(broker, handler1, handler2):
    handler_func1, results1 = handler1
    handler_func2, results2 = handler2

    broker.subscribe("topic1", handler_func1)
    broker.subscribe("topic2", handler_func2)

    broker.publish("topic1", "topice 1 idk")
    broker.publish("topic2", "THREAD CANCELLED!!!!! ANT FARM GO")

    broker.unsubscribe("topic1", handler_func1)

    broker.publish("topic1", "Hello again, topic1!")
    broker.publish("topic2", "Greetings again, topic2!")

    assert results1 == ["Handler 1: topice 1 idk"]
    assert results2 == ["Handler 2: THREAD CANCELLED!!!!! ANT FARM GO", "Handler 2: Greetings again, topic2!"]
