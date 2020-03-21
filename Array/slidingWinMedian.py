def slideWin(nums, k):
	import heapq
	res = []
	arr = nums[:k]
	heapq.heapify(arr)
	if k%2 == 0:
		val = (heapq.nlargest(k, arr))		
		res.append((val[k//2]+val[(k//2) -1])/2)
	else:
		res.append(heapq.nlargest(k, arr)[k//2])
	i = 0
	j = k
	while j < len(nums):
		arr.remove(nums[i])
		arr.append(nums[j])
		heapq.heapify(arr)
		if k%2 == 0:
			val = (heapq.nlargest(k, arr))		
			res.append((val[k//2]+val[(k//2) -1])/2)
		else:
			res.append(heapq.nlargest(k, arr)[k//2])
		i+=1
		j+=1
	return res
	
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(slideWin(nums, k))