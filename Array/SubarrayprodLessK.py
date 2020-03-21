def subarray(nums,k):
	count = 0
	i = 0
	j = 1
	prod = nums[0]
	while j < len(nums):
		prod = prod*nums[j]
		print(1, prod)
		if prod < k:
			count += 1
			j=j+1
		else:
			while prod > k:
				prod = prod/nums[i]
				print(2, prod)
				if prod < k:
					count += 1
					j=j+1
				i += 1
	print(count)
	for ele in nums:
		if ele < k:
			count = count + 1
	return count
		
			
	#while i < len(nums):							[10,5,2,6]
	#	if j < len(nums) and nums[j] < k:
	#		count += 1
	#	if j < len(nums):
	#		prod = prod*nums[j]
	#	if j < len(nums) and prod < k:
	#		count += 1
	#		j += 1
	#	elif prod >= k or j == len(nums):
	#		prod = prod//nums[i]
	#		i = i+1
	#return count
nums = [10,5,2,6]
k = 100
print(subarray(nums, 100))