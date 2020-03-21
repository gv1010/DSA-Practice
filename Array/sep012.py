def seperate(nums):
	i = 0
	j = len(nums)-1
	m = 0
	while m <= j:
		if nums[m] == 0:
			nums[i], nums[m] = nums[m], nums[i]
			m = m+1
			i = i+1
		elif nums[m] == 1:
			m = m+1
		else:
			nums[m], nums[j] = nums[j], nums[m]
			j = j-1
	return nums
nums = [1,0,0,0,1,1,2,2,0,1,1]
nums = [1,1,0,2,2,0,2]
print(seperate(nums))
#print(seperate(nums, 1,2))
			
		