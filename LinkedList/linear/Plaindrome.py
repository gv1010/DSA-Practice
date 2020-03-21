N = int(input())
arr = input()
arr = list(arr)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
		
class LinkedList:
    def __init__(self, head):
        self.head = Node(head)
		
L = LinkedList(arr[0])
node = L.head
for val in arr[1:]:
    node.next = Node(val)
	node = node.next
left = L.head
right = left
def palindrome(left, right):
	if right is None:
		return True
	if palindrome(left, right.next) and left.val == right.val:
		left = left.next
		return True
	else:
		return False
		
