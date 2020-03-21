def hashtables(nums, k, t):
	for i in range(len(nums)):
		for j in range(i+1, i+k+1):
			if j < len(nums):
				if 	abs(i-j) <= k  and abs(nums[i]-nums[j]) <= t:
					return True
	return False
	
#nums = [1,2,3,1]
nums = [1,5,9,1,5,9]
k =2
t =3
print(hashtables(nums, k, t))