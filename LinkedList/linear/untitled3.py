# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:30:49 2019

@author: citrix
"""

class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
		
	def insert_node(self,data):
        if self.head is None:
			self.head = Node(data)
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = Node(data)
		
		
	def mergeLists(head1, head2):
		merge = LinkedList()
		temp1 = head1.next
		temp2 = head2.next
		while (temp1) :
			while (temp2):
				if temp1.data > temp2.data:
					merge.insert_node(temp2.data)
					head2 = temp2.next
					break
				else:
					merge.insert_node(temp1.data)
					head1 = temp1.next
				temp2 = temp2.next
			temp1 = temp1.next
		return merge

list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2
e2.next = e3

list1.insert_node("Thursday")
		
	
		