
import heapq
minBox = []
maxBox = []
median_list = []
nums= []
count = 0
for i in range(int(input())):
	num = int(input())
	nums.append(num)
	count = count+1
	if count == 1:
		print('m', nums[0], end = "\n")
	elif count == 2:
		if nums[0] > nums[1]:
			heapq.heappush(minBox, nums[0])
			heapq.heappush(maxBox, -1*nums[1])
		else:
			heapq.heappush(minBox, nums[1])
			heapq.heappush(maxBox, -1*nums[0])
		print('m', (nums[0]+nums[1])/2, end = "\n") 
	else:
		if num >= minBox[0]:
			heapq.heappush(minBox, num)
		if num < -1*maxBox[0]:
			heapq.heappush(maxBox, -1*num)
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
		print(median, end="\n")
#nums = [1,2,3,4,5]
			