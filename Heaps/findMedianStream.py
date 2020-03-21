def medianFunc(nums):
	import heapq
	minBox = []
	maxBox = []
	median_list = []
	count = 0
	for num in nums:
		count = count + 1
		if count == 1:
			median_list.append(nums[0])
			median = nums[0]
		elif count == 2:
			if nums[0] > nums[1]:
				heapq.heappush(minBox, nums[0])
				heapq.heappush(maxBox, -1*nums[1])
			else:
				heapq.heappush(minBox, nums[1])
				heapq.heappush(maxBox, -1*nums[0])
				
			if len(minBox) - len(maxBox) == 0:
				median = (minBox[0]+(-1*maxBox[0]))/2
				median_list.append(median)
			heapq.heapify(minBox)
			heapq.heapify(maxBox)
			
		else:
			
			if num >= minBox[0]:
				heapq.heappush(minBox, num)
				heapq.heapify(minBox)
			else:
				heapq.heappush(maxBox, -1*num)
				heapq.heapify(maxBox)
			#else:
			#	if len(minBox) > len()
			'''adjustment'''
			if len(maxBox) - len(minBox) == 2:
				val = heapq.heappop(maxBox)
				heapq.heappush(minBox, -1*val)
			if len(minBox) - len(maxBox) == 2:
				val = heapq.heappop(minBox)
				heapq.heappush(maxBox, -1*val)
			'''finding median'''
			if len(maxBox) - len(minBox) == 1:
				median = -1*maxBox[0]
			if len(minBox) - len(maxBox) == 1:
				median = minBox[0]
			if len(minBox) - len(maxBox) == 0:
				median = (minBox[0]+(-1*maxBox[0]))/2
			median_list.append(median)
		print(minBox, maxBox,'---', median)
	return " ".join(map(str, median_list))


nums = [6,10,2,6,5,0,6,3,1,0,0]
nums = [12,10,13,11,5,15,1,11,6,17,14,8,17,6,4,16,8,10,2,12,0]
print(medianFunc(nums))
			