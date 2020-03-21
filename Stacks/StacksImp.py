class Node:
    def __init(self, value=None):
        self.value = value
        self.next = None
		
class Stack:
    def __init__(self):
        self.head = None
		
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
		
    def pop(self):
        temp = self.head
        print(temp.data)
        self.head = self.head.next
		
    def print_stack(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
	
	
list1 = Stack()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.head.next = e2
e2.next = e3

list1.print_stack()