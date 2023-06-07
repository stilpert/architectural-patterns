import pytest
from queue import Queue
from master import Master
from slave import Slave


@pytest.fixture
def master():
    return Master()


@pytest.fixture
def slaves(master):
    slaves = []
    for _ in range(2):
        slave = Slave(master)
        slaves.append(slave)
    return slaves


def test_add_slave(master, slaves):
    for slave in slaves:
        master.add_slave(slave)
    assert len(master.slaves) == 2


def test_add_task(master):
    task = "task1"
    master.add_task(task)
    assert not master.tasks_queue.empty()
    assert master.tasks_queue.qsize() == 1


def test_distribute_task(master, slaves):
    task = "task1"
    master.add_slave(slaves[0])
    master.distribute_task(task)
    assert not master.tasks_queue.empty()
    assert master.tasks_queue.qsize() == 1


def test_collect_results(master):
    master.results_queue.put("result1")
    master.results_queue.put("result2")
    results = master.collect_results()
    assert len(results) == 2
    assert results == ["result1", "result2"]


def test_process_tasks(master, slaves):
    tasks = ["task1", "task2", "task3"]
    for task in tasks:
        master.add_task(task)
    for slave in slaves:
        slave.start()
    master.process_tasks()
    results = master.collect_results()
    assert len(results) == 3
    assert results == ["TASK1", "TASK2", "TASK3"]
