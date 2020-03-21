def countWays(target, nums):

	#if dp[n] > -1:
	#	return dp[n]
	#count = 0
	#for i in nums:
	#	if n-i > 0:
	#		print(n-i)
	#		count = count + countWays(n-i,nums,dp)
	#	elif n-i == 0:
	#		dp[n] = count
	#		return dp[n]
	#	print(count)
	#dp[n] = count
	#return count
	
	dp = [0]*(target+1)
	for i in nums:
		if i<= target:
			dp[i] = 1
	arr = sorted(nums)
	for i in range(1,target+1):
		for k in range(len(arr)):
			if i-arr[k] >= 0:
				dp[i] = dp[i] + dp[i-arr[k]]
		
	return dp[-1]


nums = [9]
n = 4

print(countWays(n,nums))