# Node class
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		

# Stack class
class Stack:
	def __init__(self):
		self.top = None
		self.height = 0
		self.size = 0
	
	# Returns True if stack is empty.
	def is_empty(self):
		return self.size == 0
	
	# Pushes a new node to the stack.
	def push(self, value):
		new_node = Node(value)
		new_node.next = self.top
		self.top = new_node
		self.height += value
		self.size += 1
	
	# Pops the top node in the stack.
	def pop(self):
		if self.is_empty():
			raise IndexError("pop from an empty stack.")
			
		value = self.top.value
		self.top = self.top.next
		self.height -= value
		self.size -= 1
		return value
	
	# Peeks the value of the top node in the stack.
	def peek(self):
		if self.is_empty():
			raise IndexError("peek from an empty stack.")
		
		return self.top.value


# A string of dashes.
dash = "------------------------------------------------------------------------"


# Exits the program if the user wishes to, continue otherwise.
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


# main
def main():
	# Initialize a list of stacks.
	stacks = []
	# For 3 times.
	for i in range(3):
		# Append a stack to the stacks list.
		stacks.append(Stack())
		
		# Take user input to be pushed to the stack.
		user_input = input(f"Enter elements of Stack {i + 1}: ")
		
		# Split numbers separated by spaces.
		numbers = user_input.split()
		
		# For how many input number times.
		for number in numbers:
			# Ignore non numbers
			try:
				num = int(number)
				stacks[i].push(num)
			except ValueError:
				print(f"Ignoring invalid input {number}.")
				
	print(dash)
	
	# Prints the stack heights
	for i in range(3):
		print(f"Stack {i + 1} total height: {stacks[i].height}")
		
	print(dash)
	
	# While stacks have heights.
	while stacks[0].height > 0 or stacks[1].height > 0 or stacks[2].height > 0:
		# If all stacks have similar heights, print their heights.
		if stacks[0].height == stacks[1].height == stacks[2].height and stacks[0].height != 0:
			print(f"All stacks are equal at Height: {stacks[0].height}")
			for i in range(3):
				print(f"Stack {i + 1}: ", end=" ")
				while stacks[i].size > 0:
					print(stacks[i].pop(), end=" ")
				print()
			print(dash)
			cont()
		
		# Find stack with highest height.
		max_index = 0
		for i in range(3):
			if stacks[i].height > stacks[max_index].height:
				max_index = i
		
		# Pop from the stack with highest height.
		stacks[max_index].pop()
		
	
	# Print "Stack heights will never be equal."
	print("Stack heights will never be equal.")
	print(dash)
	cont()


if __name__ == "__main__":
	main()
