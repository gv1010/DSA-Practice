def partition(nums, k):
	if sum(nums)%k != 0:
		return False
	part  = sum(nums)//k
	