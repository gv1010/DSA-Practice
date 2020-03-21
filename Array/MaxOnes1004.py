def maxOnes(nums,k):
	max_Win = float('-inf')
	for i in range(len(nums)):
		val = 0
		for j in range(i, len(nums)-1):
			if nums[j] == 0:
				val = val + 1
			if val == k and (nums[j] == 0 or j == len(nums)-1):
				max_Win = max(max_Win, j-i)
				break
			elif val == k and nums[i]==1:
				max_Win = max(max_Win, j-i)
	return max_Win
def maxOnes_(nums,k):
	global_max = float('-inf')
	count = 0
	
	for _ in range(len(nums)):
		val = 0
		for i in range(_,len(nums)):
			if nums[i] == 1:
				count = count + 1
			elif val < k and nums[i] == 0:
				#global_max = max(global_max, count)
				count = count + 1
				val = val + 1
			elif val == k and nums[i] == 0:
				global_max = max(global_max, count)
				count = 0
	return max(global_max, count)
	
nums = [1,1,1,0,0,0,1,0,1,1,1,1,0]
#nums = [0,0,0,1,1,1]
k = 2
print(maxOnes_(nums, k))