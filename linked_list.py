
#Implement a singly linked list, to be used in other applications

class Node():
	#Implement a basic Node object, that has fields next (the node it points to)
	#and a value field

	def __init__(self, value=None):
		self.data = value
		self.next = None

class linkedList():
	#make a singly linked list

	def __init__(self):
		#Instantiate the linked list
		self.head = None
		self.tail = None

	def add_to_tail(self, val):
		#add a node to the list
		new_node = Node(val)
		if self.head == None:
			self.head = new_node
			self.tail = new_node
		else:
			tracker = self.head
			while tracker.next != None:
				tracker = tracker.next
			tracker.next = new_node
			self.tail = new_node


	def insert(self, previous_val, new_val):
		#Insert: given the previous node, insert a new node
		
		in_node = Node(new_val)

		#Move through the linked list, searching for previous value in node data fields
		#If we find a match, we can change the links, thus inserting the new node
		mover = self.head
		while mover.next != None:
			if mover.data == previous_val:
				in_node.next = mover.next
				mover.next = in_node
				return
			else:
				mover = mover.next

		#Make sure to check the value of the last node
		if mover.data == previous_val:
			in_node.next = mover.next
			mover.next = in_node
			return
		else:
			print("Invalid 'previous value' input.")


	def delete(self, val):
		#Given a data value, delete the node from the linked list

		if self.head == None:
			print("This list is already empty!")
			return

		elif self.head.data == val:
			print(f"Deleting {val} from Linked List.")
			self.head = None
			return

		tracker = self.head

		while tracker.next != None:
			if tracker.next.data == val:
				#Delete the node by undoing its link to previous node
				#Account for the case where desired deletion is the tail.
				if tracker.next != self.tail:
					next_node = tracker.next
					tracker.next = next_node.next
				else:
					tracker.next = None
					self.tail = tracker
				print(f"Deleting {val} from Linked List.")
				return
			else:
				tracker = tracker.next

	def pop_list(self):
		#Remove the last element of the linked list

		tracker = self.head
		ahead = tracker.next

		while ahead.next != None:
			tracker = ahead
			ahead = ahead.next
		tracker.next = None
		self.tail = tracker


	def print_list(self):
		#print the contents of the linked list in order

		#Move through the linkedlist, printing data values
		plotter = self.head
		while plotter.next != None:
			print(plotter.data)
			plotter = plotter.next
		#Print the last node's data
		print(plotter.data)


"""test = linkedList()
test.add_to_tail(5)
test.add_to_tail(10)
test.insert(10, 15)
test.add_to_tail(20)
test.print_list()
test.delete(20)
test.print_list()"""