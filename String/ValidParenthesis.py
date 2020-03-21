def valid(str):
	str = list(str)
	stack = []
	for i in str:
		if i == '(' :
			stack.append(')')
		elif i == '[':
			stack.append(']')
		elif i == '{':
			stack.append('}')
		elif i == ')':
			par = stack.pop(-1)
			if i != par:
				return False
		elif i == ']':
			par = stack.pop(-1)
			if i != par:
				return False
		elif i == '}':
			par = stack.pop(-1)
			if i != par:
				return False
	return True
	
str = "([])"
print(valid(str))
			