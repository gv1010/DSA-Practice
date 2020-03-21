class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
	
class LinkedList:
	def __init__(self, head):
		self.head = Node(head)
	def swapPairs(self,head):
		if head.next is None:
			return head
		if head.next.next is None:
			f = head
			s = head.next
			temp = f.next.next
			s.next = f
			f.next = temp
			return s
		else:
			f = head
			s = head.next
			temp = self.swapPairs(f.next.next)
			s.next = f
			f.next = temp
			return s
	def printList(self,head):
		while head:
			print(head.val, end = "-")
			head = head.next
			
l = LinkedList(1)
#l.head.next = Node(2)
#l.head.next.next = Node(3)
#l.head.next.next.next = Node(4)

l.printList(l.head)
print()
print('-'*70)
node = l.swapPairs(l.head)
l.printList(node)
		
			
	