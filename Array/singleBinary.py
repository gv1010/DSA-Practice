def search(nums):
	start = 0 
	end = len(nums)-1
	while start<=end:
		mid = (start+end)//2
		if mid >= 1 and nums[mid] == nums[mid-1]:
			if (mid - start - 1)%2 == 0:
				start = mid+1
			else:
				end = mid-1
		elif mid < len(nums)-1 and nums[mid] == nums[mid+1]:
			if (mid - start)%2 == 0:
				start = mid+2
			else:
				end = mid
		else:
			return mid
nums = [1,1,2,3,3,4,4,5,5]
nums = [3,3,7,7,10,11,11]
print(search(nums))

				