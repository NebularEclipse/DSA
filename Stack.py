class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		

class Stack:
	def __init__(self):
		self.top = None
		self.height = 0
		self.size = 0
		
	def is_empty(self):
		return self.size == 0
			
	def push(self, value):
		new_node = Node(value)
		new_node.next = self.top
		self.top = new_node
		self.height += value
		self.size += 1
		
	def pop(self):
		if self.is_empty():
			raise IndexError("pop from an empty stack.")
			
		value = self.top.value
		self.top = self.top.next
		self.height -= value
		self.size -= 1
		return value
		
	def peek(self):
		if self.is_empty():
			raise IndexError("peek from an empty stack.")
		
		return self.top.value


dash = "------------------------------------------------------------------------"


def cont():
	user_input = input("Continue? Y or N? ").lower()
	if user_input == "y":
    print(dash)
		main()
	elif user_inout == "n":
		input("Thank you!")
		exit()
	else:
		cont():


def main():
	stacks = []
	for i in range(3):
		user_input = input(f"Enter elements of Stack {i + 1}: ")
		numbers = user_input.split()
		for number in numbers:
			try:
				num = int(number)
				stacks[i].push(num)
			except ValueError:
				print(f"Ignoring invalid input {number}.")
				
	print(dash)
	
	for i in range(3):
		print(f"Stack {i + 1} total height: {stacks[i].height}")
		
	print(dash)
	
	while stacks[0].height > 0 or stacks[1].height > 0 or stacks[2].height > 0:
		max_index = 0
		for i in range(3):
			if stacks[i].height > stacks[max_index]:
				max_index = i
				
		stacks[max_index].pop()
		
		if stacks[0].height == stacks[1].height == stacks[2].height:
			print(f"All stacks are equal at Height: {stacks[0].height}")
			for i in range(3):
				print(f"Stack {i + 1}: ", end=" ")
				while stacks[i].size > 0:
					print(stacks[i].pop(), end=" ")
				print()
			cont()
		
	print("Stack heights will never be equal.")
	cont()


if __name__ == "__main__":
	main()
