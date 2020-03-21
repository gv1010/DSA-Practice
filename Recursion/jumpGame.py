def minJump(nums,idx):
	if idx >= len(nums):
		return 0
	result = float('inf')

	for i in range(idx+1, nums[idx]+1):
		value = 1+minJump(nums, i)
		result = min(value, result)
	return result 
	
def minJumps(nums):
	jumps = [0]*len(nums)
	for i in range(1, len(nums)):
		jumps[i] = float('inf')
		for j in range(i):
			if i <= j+nums[j] and jumps[j] != float('inf'):
				jumps[i] = min(jumps[i], jumps[j]+1)
	return jumps[len(nums)-1]
nums = [1,1,1,1,1,1]
nums = [1,2,1]
nums = [1,4,3,2,6,7]
nums = [3,2,1,0,4]
#nums = [1,3,5,8,9,2,6,7,6,8,9]
print(minJumps(nums))