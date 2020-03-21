from collections import defaultdict
def findMin(nums):
	add = 0
	store = defaultdict(int)
	glbMin = float('inf')
	for i in range(len(nums)):
		add = add + nums[i]
		store[i] = add
	for i in range(len(nums)):
		value = store[len(nums)-1]-store[i] -store[i]
		if value > 0 and value in nums:
			glbMin = min(glbMin, value)
	if glbMin > 0 and glbMin != float('inf'):
		return glbMin
	return -1
	
nums = [0,2,3]
print(findMin(nums))