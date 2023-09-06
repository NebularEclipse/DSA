dash = "------------------------------------------"
menu = """[0] Exit
[1] Enqueue Workload
[2] Dequeue Workload"""

class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

    def workload(self):
        count = 0
        for i in self.queue:
            count += i
            print(i)
        return count
    
    def display(self):
        print(self.queue)

