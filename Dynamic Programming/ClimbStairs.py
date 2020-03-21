def Stairs(value):
	stairs = dict()
	stairs[0] = 0
	stairs[1] = 1
	stairs[2] = 2
	for i in range(3,value+1):
		#if i not in stairs.values():
		stairs[i] = stairs[i-1] + stairs[i-2]
	return stairs[value]
	
	
print(Stairs(3))