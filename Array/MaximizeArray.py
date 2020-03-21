def validTrinagle(nums):
	nums = sorted(nums)
	count = 0
	
	for i in range(len(nums)-2):
		k = i+2
		for j in range(i+1, len(nums)-1):
			while k < len(nums) and nums[i]+nums[j] > nums[k]:
				k = k + 1
			print(i,j,k)
			count = count + k-j-1
	return count
		
arr = [2,2,3,4]
print(validTrinagle(arr))