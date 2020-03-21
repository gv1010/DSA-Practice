def perform(i, l, s, e,maxVal):
	if l == 0:
		return sum(s)*min(e)
	
	for j in range(i, n):
		maxVal = max(maxVal, perform(j+1, l-1, s+[speed[j]], e+[efficiency[j]],maxVal))
		print(maxVal)
	return maxVal
	
maxVal = float('-inf')
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
n = 3
speed = [2,8,2]
efficiency = [2,7,1]
k = 2

i = 0 
l = k
s = []
e = []
print(perform(i,l,s,e,maxVal))