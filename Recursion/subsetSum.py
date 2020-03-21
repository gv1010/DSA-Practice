def subsetSum(target, list):
	if target == 0:
		return True
	if list == []:
		return False
	res = False
	
	for i in range(len(list)):
		if target-list[i] >= 0:
			res = res or subsetSum(target-list[i], list[i+1:])
	return res
		
list = [3, 34, 4, 12, 5, 2]
target = 9
print(subsetSum(target, list))