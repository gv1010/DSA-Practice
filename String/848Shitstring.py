def shiftString(S, shifts):

	val = 0
	new = []
	for i in shifts[::-1]:
		val = i + val
		new.insert(0, val)
	res = ""
	for idx, s in enumerate(S):
		if idx < len(new):
			shift = ord(s)-ord('a') + new[idx]
			shift = shift%26
			res = res + chr(ord('a')+shift)
		else:
			res = res + s
	return res
		
S = "abc"
shifts = []
print(shiftString(S, shifts))
