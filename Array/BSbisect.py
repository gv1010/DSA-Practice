def bisecttt(nums,e):
	import bisect 
	return bisect.bisect_left(nums, e)
nums = [4,5,6,7,8]
e = 4
print(bisecttt(nums, e))