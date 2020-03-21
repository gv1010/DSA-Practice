def minimumSubarry(nums, s):
	i = 0 
	j = 0
	sub_sum = nums[i]
	count = float('inf')
	while i < len(nums)-1:
		
		if j < len(nums)-1 and sub_sum < s:
			j = j+1
			sub_sum = sub_sum+nums[j]
		elif sub_sum == s:
			count = min(j-i+1, count)
			sub_sum = sub_sum-nums[i]
			i = i+1
		else:
			break
	if count != float('inf'):	
		return count
	else:
		return 0
nums = [2,3,-1,2,-4,3]
s = 7
print(minimumSubarry(nums, s))
			