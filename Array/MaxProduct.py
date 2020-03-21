def maxProduct(nums):
	max1 = float('-inf')
	max2 = float('-inf')
	max3 = float('-inf')
	min1 = float('inf')
	min2 = float('inf')
	for i in range(len(nums)):
		if nums[i] > max1:
			max2 = max1
			max1 = nums[i]
		elif nums[i] > max2:
			max3 = max2
			max2 = nums[i]
		elif nums[i] > max3:
			max3 = nums[i]
		if nums[i] < min1:
			min2  = min1
			min1 = nums[i]
		elif nums[i] < min2:
			min2 = nums[i]
	return max1, max2, max3, min1, min2
	return max(max1*min1*min2, max1*max2*max3)
nums = [1,2,3,4]
print(maxProduct(nums))