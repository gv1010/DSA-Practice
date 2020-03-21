def letter(digits, index, path, res):
	if index == len(digits):
		return res.append(path)
	
	numPad = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv', '9':'wxyz'}
	
	s = digits[index]
	for i in numPad[s]:
		letter(digits, index+1, path+i, res)
	
digits = '234'
index = 0
path = ""
res = []	
print(letter(digits, index, path, res))
print(res)
		
		
	