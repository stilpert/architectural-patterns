import time
from threading import Thread

class Slave(Thread):
    def __init__(self, master):
        super().__init__()
        self.master = master


    def run(self):
        while True:
            task = self.master.tasks_queue.get()
            if task is None:
                self.master.tasks_queue.task_done()
                break
            result = self.process_task(task)
            self.master.results_queue.put(result)
            self.master.tasks_queue.task_done()


    def process_task(self, task):
        time.sleep(1)
        return task.upper()
