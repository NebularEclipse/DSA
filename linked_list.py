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
		
		response = int(input())
		
		if response == 0:
			self.head = None
			exit()
		elif response == 1:
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
