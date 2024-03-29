"""
BSCS 2B
Group 4
Members:
	Abellera, Alvin Dave D.
	Bata, Gian Carlo B.
	Olores, Kaye Khrysna C.
"""

from sys import platform
from os import system


# The string for the menu.
menu = """
[0]  Exit
[1]  Insert At Start
[2]  Insert At End
[3]  Insert At Position
[4]  Delete At Start
[5]  Delete At End
[6]  Delete At Position
[7]  Delete Number
[8]  Search Number
[9]  Display Number At Position
[10] Display List
"""

# String templates.
option_text = "Please choose an option: "
int_text = "Enter an integer: "
pos_text = "Enter position: "
val_text = "Enter a value: "


# Rids the console of texts.
def clear():
	if platform.startswith("win"):
		system("cls")
	else:
		system("clear")


# A node object.
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


# A linked list object
class LinkedList:
	def __init__(self):
		self.head = None
	
	# Method to terminate the program.
	def terminate(self):
		print("Are you sure you want to exit?")
		print("[0] Yes")
		print("[1] No")
		
		try:
			response = int(input(option_text))
		except ValueError:
			clear()
			self.terminate()
			return

		if response == 0:
			self.head = None
			clear()
			print("Thank you!")
			input("Press Enter to exit...")
			clear()
			exit()
		elif response == 1:
			clear()
			return
		else:
			clear()
			self.terminate()
			return
			
	# Method to insert an element at the beginning of the list.
	def insert_start(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		
		print(f"You've inserted {data} to the start of the list.")
		
	# Method to insert an element at the end of the list.
	def insert_end(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = new_node
			
		print(f"You've inserted {data} to the end of the list.")
		
	# Method to insert an element at a specified position in the list.
	def insert_at(self, data, position):
		if position == 1:
			self.insert_start(data)
			return

		new = Node(data)
		temp = self.head
		for i in range(2, position):
			if temp.next is not None:
				temp = temp.next
			else:
				print("Position invalid.")
				return
		new.next = temp.next
		temp.next = new
		
		print(f"You've inserted {data} to position {position} of the list.")
		
	#Method to delete the first element in the list.
	def delete_start(self):
		if self.head is None:
			print("The list is empty.")
			return
			
		deleted = self.head.data
		self.head = self.head.next
		print(f"You've deleted {deleted} from the start of the list.")
	
	# Method to delete the last element in the list.
	def delete_end(self):
		if self.head is None:
			print("The list is empty.")
			return

		if self.head.next is None:
			deleted = self.head.data
			self.head = None
			print(f"You've deleted {deleted} from the end of the list.")

		temp = self.head
		while temp.next.next is not None:
			temp = temp.next
		deleted = temp.next.data
		temp.next = None
		print(f"You've deleted {deleted} from the end of the list.")
	
	# Method to delete at a specified position
	def delete_at(self, position):
		if position == 1 and self.head is not None:
			deleted = self.head.data
			self.delete_start()
			print(f"You've deleted {deleted} from position {position} of the list.")
			return

		temp = self.head
		for i in range(2, position):
			if temp.next is not None:
				temp = temp.next
			else:
				print("Position invalid.")
				return
		deleted = temp.next.data
		temp.next = temp.next.next
		print(f"You've deleted {deleted} from position {position} of the list.")
	
	# Method to delete a value if found.
	def delete_value(self, target):
		if self.head is None:
			print("The list is empty.")
			return

		if self.head.data == target:
			self.delete_start()
			print(f"{target} has been successfully deleted.")
			return

		temp = self.head
		while temp.next is not None:
			if temp.next.data == target:
				temp.next = temp.next.next
				print(f"{target} has been successfully deleted.")
				return
			temp = temp.next

		print(f"{target} is not on the list and cannot be deleted.")
	
	# Method to search for a value.
	def find(self, target):
		if self.head is None:
			print("The list is empty.")
			return

		temp = self.head
		count = 1
		while temp.data != target and temp.next is not None:
			temp = temp.next
			count += 1
		if temp.data == target:
			print(f"Value found at position {count}.")
			return
		else:
			print("Value not found.")
	
	# Method to display an element at a position.
	def display_at(self, position):
		if self.head is None:
			print("The list is empty.")
			return
			
		temp = self.head
		for i in range(1, position):
			if temp.next is not None:
				temp = temp.next
			else:
				print("Position exceeds the size of the list.")
				return
		print(f"The value at position {position} is {temp.data}.")
		
	# Method to display all elements in the list.
	def display(self):
		temp = self.head
		print("head", end=" -> ")
		while temp:
			print(temp.data, end=" -> ")
			temp = temp.next
		print("None")
		print()


# Driver code
def main():
	list = LinkedList()
	clear()
	
	# Command loop.
	while True:
		print(menu)
		i = int(input(option_text))
		clear()
		
		# Execute what the user chose.
		if i == 0:
			list.terminate()
		elif i == 1:
			while True:
				try:
					val = int(input(int_text))
				except ValueError:
					clear()
					continue
				else:
					break

			list.insert_start(val)
		elif i == 2:
			while True:
				try:
					val = int(input(int_text))
				except ValueError:
					clear()
					continue
				else:
					break

			list.insert_end(val)
		elif i == 3:
			while True:
				try:
					val = int(input(int_text))
				except ValueError:
					clear()
					continue
				else:
					break
			while True:
				try:
					pos = int(input(pos_text))
				except ValueError:
					clear()
					continue
				else:
					break

			list.insert_at(val, pos)
		elif i == 4:
			list.delete_start()
		elif i == 5:
			list.delete_end()
		elif i == 6:
			while True:
				try:
					pos = int(input(pos_text))
				except ValueError:
					clear()
					continue
				else:
					break

			list.delete_at(pos)
		elif i == 7:
			list.delete_value(int(input(val_text)))
		elif i == 8:
			list.find(int(input(val_text)))
		elif i == 9:
			list.display_at(int(input(pos_text)))
		elif i == 10:
			list.display()
		else:
			main()
		

# Run the driver code.
if __name__ == "__main__":
	main()