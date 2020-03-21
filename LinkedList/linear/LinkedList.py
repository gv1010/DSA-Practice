# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:29:58 2019

@author: citrix
"""

class Node:
    def __init__(self,data=None):
        self.dataval = data
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None
        
    def insertnode(self):
        print('No of elements to be added')
        inp = int(input())
        list2 = LinkedList()
        x = list2.headval
        for i in range(inp):
            val = (input())
            x = Node(val)
            x = x.nextval
        
    def printlist(self):
        printval = self.headval
        #print(printval)
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
    
        
list1 = LinkedList()

list1.insertnode()
list1.printlist()

list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2
e2.nextval = e3


list1.printlist()  
    