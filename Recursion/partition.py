def partition(nums):
	target = sum(nums)
	if target%2 != 0:
		return False
	target = target//2
	dp = [False]*(target+1)
	if max(nums) > target:
		return False
	for j in nums:
		for i in range(target+1):
			if i == 0:
				dp[i] = True 	
			if i>=j and i - j != j :
				dp[i] = dp[i-j] | dp[i]
	print(target)
	print(dp)
	return dp[-1]
	
#nums = [1,3,5,11]
nums = [2,2,3,5]
nums = [1,1,1,1]
print(partition(nums))
				
			