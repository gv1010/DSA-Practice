# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:25:13 2019

@author: citrix
"""

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        
    #new node at the beginning
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def listprint(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next
            
    def InsertAtEnd(self,data):
        
        print(self.head.data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

list1 = LinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2
e2.next = e3

list1.InsertAtEnd("Thursday")

list1.listprint()


        
    

