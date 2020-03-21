def threeSum(nums,target):
	mini = float('inf')
	list1 = []
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			for k in range(j+1, len(nums)):
				sum_ = nums[i]+nums[j]+nums[k]
				list1.append(sum_)
	print(list1)
nums = [-1, 2, 1, -4]
threeSum(nums, target = 2)
