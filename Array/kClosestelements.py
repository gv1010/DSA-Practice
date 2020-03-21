def kclosest(nums, k, x):
	s = 0
	e = len(nums)-1
	while s<=e:
		m = s + (e-s)//2
		#print(s,e)
		if nums[m] > x:
			e = m-1
		elif nums[m] < x:
			s = m+1
		else:
			return m, 1
	#print(m)
	return m,-1
def funct(nums,k,x):

	index, flag = kclosest(nums, k, x)
	print(index)
	result = []
	if flag != -1:
		if index - k//2 >= 0:
			print(1)
			result = nums[index-k//2: index]
		elif index - k//2 < 0:
			print(2)
			result = nums[:index]
		if index + k//2 >= len(nums)-1:
			print(3)
			result.extend(nums[index:index+ k-len(result) ])
		elif index + k//2 < len(nums)-1:
			print(4)
			result.extend(nums[index:k-len(result)])
		
	else:
		if index == 0:
			print(11)
			result = nums[:k]
		elif index == len(nums)-1:
			print(22)
			result = nums[len(nums)-k:]
		elif index >= k//2:
			print(33, index, k)
			result = nums[index-k//2:index + k//2+1]
	return result
	
nums = [1,1,1,10,10,10]
k = 1
x = 9
print(funct(nums,k,x))
		