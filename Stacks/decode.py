def decode(s):
	currnum = 1
	t = ""
	res = ""
	stack = []
	for i in s:
		if i == "[":
			stack.append(t)
			stack.append(curr)
			t = ""
			curr = 1
		elif i == "]":
			num = stack.pop()
			prev = stack.pop()
			print(res)
			res = res + prev + int(num)*t
			t = ""
			print(res)
			curr = 1
		elif i.isnumeric():
			curr = i
		else:
			t = t+i
			curr = 1
	return res
s = "a3[b3[e]]2[c]"
s = "3[a2[c]]"
print(decode(s))
		