from queue import Queue

class Master:
    def __init__(self):
        self.tasks_queue = Queue()
        self.results_queue = Queue()
        self.slaves = []


    def add_slave(self, slave):
        self.slaves.append(slave)


    def add_task(self, task):
        self.tasks_queue.put(task)


    def process_tasks(self):
        for slave in self.slaves:
            slave.start()

        self.tasks_queue.join()

        for _ in self.slaves:
            self.tasks_queue.put(None)

        for slave in self.slaves:
            slave.join()


    def distribute_task(self, task):
        for slave in self.slaves:
            self.tasks_queue.put(task)


    def collect_results(self):
        results = []
        while not self.results_queue.empty():
            result = self.results_queue.get()
            results.append(result)
        return results

