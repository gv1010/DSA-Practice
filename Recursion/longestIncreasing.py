def lis(nums):
	cache = [1]*len(nums)
	for i in range(len(nums)):
		max_res = 1
		for j in range(i):
			count = 1
			if nums[j] < nums[i]:
				count = 1 + cache[j]
			max_res = max(max_res, count)
		cache[i] = max_res
	print(cache)
	return cache[len(nums)-1]
	
nums = [4,10,4,3,8,9]
#nums = [1,2,3,4]
print(lis(nums))