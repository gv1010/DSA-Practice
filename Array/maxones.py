def maxOnes(nums):
	i = 0
	j = 0
	maxWin = float('-inf')
	for j in range(len(nums)):
		if (nums[j] == 1 or nums[j] == 0) :
			maxWin = max(maxWin, j-i+1)
		else:
			i = j+1
	return maxWin
	
def maxConsecOnes(nums, k):
	i = 0
	j = 0
	count = 0
	maxWin = float('-inf')
	while j < len(nums):
		if nums[j] == 1:
			j = j+1
		elif j < len(nums) and nums[j] == 0 and count <= k:
			j = j+1
			count = count+1
		if j < len(nums) and count > k and nums[j] == 0:
			if nums[i] == 0:
				count = count - 1
			i = i+1
		maxWin = max(maxWin, j-i+1)
		print(maxWin)
	return maxWin
nums = [1,1,1,0,0,0,1,1,1,1,0]
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
#nums = [1,1,1,0,0]
k = 3
print(maxConsecOnes(nums, k))
	