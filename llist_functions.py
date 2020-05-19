#By Michael Solimano 2020

from linked_list import Node
from linked_list import linkedList

#Problem One: Write code to remove duplicates from an unsorted linked list

def remove_dups(in_list):
	#Move through a linked list and delete nodes with duplicate values
	llist = in_list
	#Create a list to track values that have already occurred:
	list_values = []
	tracker = llist.head

	while tracker.next != None:
		ahead = tracker.next
		if ahead.data in list_values:
			print(f"Removing {ahead.data}")
			if ahead.next != None:
				tracker.next = ahead.next
			else:
				tracker.next = None
				llist.tail = tracker
		else:
			list_values.append(ahead.data)
		tracker = ahead

	#Check the last node (in case desired dup is tail)
	#Use pop_list defined in imported class if this is the case to remove tail
	if tracker.next == None:
		if tracker.data in list_values:
			llist.pop_list()


	return llist

#Problem: Return the kth to last element of a singly linked list

def return_k(llist, k):
	# function to return element k in a linked list

	tracker = llist.head
	counter = 0
	while tracker.next != None:
		if counter == k:
			return tracker.data
		else:
			counter += 1
			tracker = tracker.next
	print("Invalid input.")

#Problem: Delete a given node from the middle of a Linked List

def delete_middle(llist, node):
	#remove a given node from a linked list

	tracker = llist.head

	while tracker.next != None:
		ahead = tracker.next
		if node == ahead:
			tracker.next = ahead.next
			return
		else:
			tracker = ahead

#Problem: Check if a linked list is a palindrome

def linked_palindrome(double_llist):
	#A method to see if a doubly linked list is a palindrome
	front = double_llist.head
	back = double_llist.tail

	#Move trackers (front to back and back to front) towards the middle until they meet
	#So long as their values are equal, the palindrome is maintained.
	while front != back:
		front_data = str(front.data)
		back_data = str(back.data)
		if front_data == back_data:
			front = front.next
			back = back.prev
		else:
			print("Not a palindrome!")
			return
	print("This linked list is a palindrome!")

def single_palindrome(llist):
	#A method to see if a single linked list is a palindrome.

	#Place all linked list data values in a list.
	#This is slow, but necessary as we don't have access to previous nodes.
	#By using a list, we effectively get this access with negative indexing.

	list_values = []
	tracker = llist.head

	while tracker != None:
		list_values.append(tracker.data)
		tracker = tracker.next

	#Now, create a reversed list and compare it to the data list.
	#If equal, the Linked List was a palindrome.

	#Creating reverse list by popping from a copy of data values.
	copy = []
	for a in list_values:
		copy.append(a)
	reverse_data = []
	length = len(copy)
	counter = 0
	while counter < length:
		popped = copy.pop()
		print(counter)
		reverse_data.append(popped)
		counter += 1
	
	#Compare the linked list data set to its reversal.
	#If equal, the data is a palindrome.
	if reverse_data == list_values:
		print("Yes, this is a palindrome!")
	else:
		print("Not a palindrome!")

test_two = linkedList()
test_two.add_to_tail("a")
test_two.add_to_tail("a")
test_two.add_to_tail("b")
test_two.add_to_tail("a")
test_two.add_to_tail("a")
single_palindrome(test_two)

test = linkedList()
test.add_to_tail(5)
test.add_to_tail(10)
test.insert(10, 15)
test.add_to_tail(20)
test.add_to_tail(15)
test.add_to_tail(20)
test.add_to_tail(10)
test.print_list()
val = return_k(llist=test, k=4)
print(f"Returned value is {val}.")
print("********")
cleaned = remove_dups(test)
cleaned.print_list()


