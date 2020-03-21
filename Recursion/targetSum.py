def target(nums, S):
	prev = [0]*3001
	prev[1000] = 1
	arrSum = sum(nums)
	for num in nums:
		dp = [0]*3001
		for i in range(-arrSum, arrSum+1):
				dp[1000+i] = prev[1000+i+num] + prev[1000+i-num]
		prev = dp
	return dp[1000+S]
		
	

	
S = 3
nums = [1,1,1,1,1]
nums = [20,48,33,16,19,44,14,31,42,34,38,32,27,7,22,22,48,18,48,39]
S = 1
#nums = [2,20,24,38,44,21,45,48,30,48,14,9,21,10,46,46,12,48,12,38]
#S = 48
print(target(nums, S))