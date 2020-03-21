def maxProduct(nums, k):
	i = 0
	j = 0
	prod = nums[0]
	temp = float('inf')
	count = 0
	while j < len(nums)-2:
		if nums[j+1] < k and temp != j:
			j = temp
			count= count +1
		elif nums[j+1] >= k:
			j = j+2
			i = j
		if nums[j+1]*prod < k:
			prod = nums[j+1]*prod
			count = count + 1
			j = j+1
		else:
			prod = prod/nums[i]
			i = i+1
			
nums = [10,5,2,6]
k = 100
print(maxProduct(nums,k))