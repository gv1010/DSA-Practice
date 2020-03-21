class stacks:
	def __init__(self):
		self.items = []
	def push(self, data):
		self.items.append(data)
	def pop(self):
		return self.items.pop()
	def isempty(self):
		return self.items == []
	def get_stack(self):
		return self.items
		
s = stacks()

s.push('1')
s.push('2')
s.push('3')
print(s.get_stack())
s.pop()
print(s.get_stack())	