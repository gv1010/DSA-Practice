# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:02:52 2019

@author: citrix
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def InsertAtStart(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def listprint(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next
        
list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2
e2.next = e3

list1.InsertAtStart('Thursday')
list1.listprint()
        
        