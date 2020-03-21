def minCost(arr):
	if len(arr) == 1:
		return arr[0], 0
	if len(arr) == 2:
		return max(arr), arr[0]*arr[1]
	result = float('inf')
	for i in range(1,len(arr)):
		leftMax, leftRes = minCost(arr[:i])
		rightMax, rightRes = minCost(arr[i:])
		store = (leftRes + rightRes + leftMax*rightMax)
		print(store)
		result = min(result, store)
	return max(arr),result
	
arr = [6,2,4]
print(minCost(arr))