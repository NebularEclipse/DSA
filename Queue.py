class Queue:
	def __init__(self):
		self.queue = []
		self.workload = 0
	
	def size(self):
		return len(self.queue)
		
	def enqueue(self, value):
		self.queue.append(value)
		self.workload += value
	
	def dequeue(self):
		if self.size() == 0:
			print("The queue is empty")
			return None
		self.workload -= self.queue.pop(0)
		
	def display(self):
		if self.size() == 0:
			print("Empty")
		else:
			print(self.queue)
			

class Workload:
	def __init__(self, size):
		self.size = size
		self.queues = [Queue() for _ in range(self.size)]
		
	def enqueue_w(self, value):
		min = 0
		
		for i in range(1, self.size):
			if self.queues[i].workload < self.queues[min].workload:
				min = i

		self.queues[min].enqueue(value)
		
	def dequeue_w(self):
		min = 0
		
		for i in range(1, self.size):
			if self.queues[i].queue[0] < self.queues[min].queue[0] and self.queues[i].size() != 0:
				min = i
		
		self.queues[min].dequeue()
	
	def display(self):
		for i in range(self.size):
			print(f"Queue {i + 1}: ", end="")
			self.queues[i].display()
			

def get_int(prompt):
	try:
		return int(input(prompt))
	except ValueError:
		print("Please enter an integer")
		return get_int(prompt)


def terminate():
	prompt = """Are you sure you want to exit?
	[0] Yes
	[1] No
	Choice: """
	
	choice = get_int(prompt)
	
	if choice == 0:
		input("Thank you!")
		exit()
	elif choice == 1:
		return None
	else:
		return terminate()
		

def menu(queues):
	menu = """[0] Exit
	[1] Enqueue workload
	[2] Dequeue workload
	Choice: """
	
	choice = get_int(menu)
	
	if choice == 0:
		terminate()
	elif choice == 1:
		value = get_int("Input Value of Workload: )
		queues.enqueue_w(value)
		queues.display()
	elif choice == 2:
		queues.dequeue_w()
		queues.display()
	else:
		print("Invalid choice")


def main():
	queues = Workload()
	dash = "--------------------------------"
	while True:
		menu(queues)
		print(dash)
		

if __name__ == "__main__":
	main()