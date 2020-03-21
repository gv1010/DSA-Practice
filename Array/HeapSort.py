def Heapify(nums, n ,i):
	root = i
	l = 2*i + 1
	r = 2*i + 2
	if l < n and nums[i] < nums[l]:
		root = l
	if r < n and nums[root] < nums[r]:
		root = r
	if root != i:
		nums[i], nums[root] = nums[root], nums[i]
		Heapify(nums, n,root)
	return nums
		
	

	
nums = [4,3,5,7,1,6,2]
n = len(nums)
# Implement 
for i in range(n, -1,-1):
	Heapify(nums, n , i)
for i in range(n-1, 0, -1):
	nums[0], nums[i] = nums[i], nums[0]
	Heapify(nums, i, 0)
print(nums)
#for i in range(len(nums)):	
#	print(Heapify(nums,n, i))