# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:05:30 2019

@author: citrix
"""

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next
    
    def InsertAfter(self,prev_node,data):
        new_data = Node(data)
        new_data.next = prev_node.next
        prev_node.next = new_data

list1 = LinkedList()
list1.head = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')

list1.head.next = e2
e2.next = e3

list1.InsertAfter(list1.head.next, 'WOOOO')
list1.listprint()

        