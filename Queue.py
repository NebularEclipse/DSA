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
    
    def peek(self):
        if self.size() > 0:
            return self.queue[0]
        return None
    
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


class Workload():
    def __init__(self):
        self.q = []
        for i in range(3):
            self.q.append(Queue())

    def workload_enqueue(self, value):
        min = 0
        for i in range(3):
            if self.q[i].workload() < self.q[min].workload():
                min = i

        self.q[min].enqueue(value)

    def workload_dequeue(self):
        min = 0
        for i in range(3):
            if self.q[i].peek() < self.q[min].peek():
                min = i

        return self.q[min].dequeue()
