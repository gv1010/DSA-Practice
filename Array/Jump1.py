def jump(nums):
	length = len(nums)-1
	i = 0
	while i<=length and nums[i] != 0:
		i = i+nums[i]
		if i == length:
			return True
	return False
nums = [2,3,1,0,4]
print(jump(nums))
'''suicide for this logic'''