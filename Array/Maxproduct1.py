def maxProduct(nums, k):
	i = 0
	j = 0
	prod = 1
	temp = float('inf')
	count = 0
	while j < len(nums):
		prod = prod * nums[j]
		while prod >= k:
			prod = prod//nums[i]
			i = i+1
		count = count + j-i+1
		j = j +1
	return count
			

	return count
nums = [10,5,2,6]
k = 100
print(maxProduct(nums,k))