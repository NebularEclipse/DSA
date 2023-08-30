from sys import platform
from os import system


def clear():
	if platform.startswith("win"):
		system("cls")
	else:
		system("clear")


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def terminate(self):
		print("Are you sure you want to exit?")
		print("[0] Yes")
		print("[1] No")

		response = int(input("Enter option: "))

		if response == 0:
			self.head = None
			clear()
			print("Thank you!")
			exit()
		elif response == 1:
			clear()
			return
		else:
			clear()
			self.terminate()
			return

	def insert_start(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_end(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next is not None:
				temp = temp.next
			temp.next = new_node

	def insert_at(self, data, position):
		if position == 1:
			self.insert_start(data)
			return

		new = Node(data)
		temp = self.head
		for i in range(2, position):
			temp = temp.next
		new.next = temp.next
		temp.next = new

	def delete_start(self):
		if self.head is None:
			return

		self.head = self.head.next

	def delete_end(self):
		if self.head is None:
			return

		if self.head.next is None:
			self.head = None

		temp = self.head
		while temp.next.next is not None:
			temp = temp.next
		temp.next = None

	def delete_at(self, position):
		if position == 1 and self.head is not None:
			self.delete_start()
			return

		temp = self.head
		for i in range(2, position):
			temp = temp.next
		temp.next = temp.next.next

	def delete_value(self, target):
		if self.head is None:
			print(f"{target} is not on the list and cannot be deleted.")
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
			temp = temp.next

		print(f"{target} is not on the list and cannot be deleted.")

	def find(self, target):
		if self.head is None:
			print("Value not found.")
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

	def display_at(self, position):
		temp = self.head
		for i in range(1, position):
			temp = temp.next
		print(temp.data)

	def display(self):
		temp = self.head
		print("head", end=" -> ")
		while temp:
			print(temp.data, end=" -> ")
			temp = temp.next
		print("None")
		print()
		
def main():
	list = LinkedList()
	clear()
	while True:
		print("[0]  Exit")
		print("[1]  Insert At Start")
		print("[2]  Insert At End")
		print("[3]  Insert At Position")
		print("[4]  Delete At Start")
		print("[5]  Delete At End")
		print("[6]  Delete At Position")
		print("[7]  Delete Number")
		print("[8]  Search Number")
		print("[9]  Display Number At Position")
		print("[10] Display List")
		i = int(input("Enter option: "))
		clear()
		if i == 0:
			list.terminate()
		elif i == 1:
			list.insert_start(int(input("Enter number: ")))
		elif i == 2:
			list.insert_end(int(input("Enter number: ")))
		elif i == 3:
			list.insert_at(int(input("Enter number: ")), int(input("Enter position: ")))
		elif i == 4:
			list.delete_start()
		elif i == 5:
			list.delete_end()
		elif i == 6:
			list.delete_at(int(input("Enter position: ")))
		elif i == 7:
			list.delete_value(int(input("Enter value: ")))
		elif i == 8:
			list.find(int(input("Enter value: ")))
		elif i == 9:
			list.display_at(int(input("Enter position: ")))
		elif i == 10:
			list.display()
		else:
			main()
		

if __name__ == "__main__":
	main()