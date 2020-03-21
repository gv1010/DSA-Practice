def niceSub(nums):
	arr = []
	for i in range(len(nums)):
		arr.append(nums[i]%2)
	sumMap = {0:1}
	val = 0
	count = 0
	for i in range(len(arr)):
		val = val+arr[i]
		if val-k in sumMap:
			count = count + sumMap[val-k]
		if val in sumMap:
			sumMap[val] = sumMap[val]+1
		else:
			sumMap[val] = 1
	return count
nums = [2,1,4,5,6,3]
k = 2 
print(niceSub(nums))

		
