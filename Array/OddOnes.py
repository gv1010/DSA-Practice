#Write a Program for Find the Number Occurring Odd Number of Times
class Arrays:
	def __init__(self, arr):
		self.arr = arr
	def func( arr):
		store = dict()
		odd = None
		for i in arr:
			if i not in store:
				store[i] = 1
			else:
				store[i] = store[i] + 1
			if store[i]%2 == 1:
				odd = i
		if odd is None:
			return None
		return odd
	#arr = [1,2,3,3,3,2,1]
	#print(func(arr))

	def func_01s(self, arr):
		left = 0
		right = len(arr)-1
		while left < right:
			if arr[left] > arr[right]:
				temp = arr[left]
				arr[left] = arr[right]
				arr[right] = temp
				left = left + 1
				right = right - 1
			if arr[left] != 1:
				left = left + 1
			if arr[right] != 0:
				right = right - 1
		return arr


#
#print(Arrays.func_01s(arr))
	def Dutch(self, arr):
		l = 0
		m = 0
		h = len(arr)-1
		while (m<=h):
			if arr[m] == 0:
				arr[l], arr[m] = arr[m], arr[l]
				m = m+1
				l = l+1
			elif arr[m] == 1:
				m = m+1
			elif arr[m] == 2:
				arr[h], arr[m] = arr[m], arr[h]
				h = h-1

		return arr

	def waveForm(self, arr):
		for i in range(len(arr)-1):
			if i%2 == 0 and arr[i] < arr[i+1]:
				temp = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = temp
			if i%2 == 1 and arr[i] > arr[i+1]:
				temp = arr[i+1]
				arr[i+1] = arr[i]
				arr[i] = temp
		return arr


	#Write a Program for Maximum difference between two elements such that
	#larger element appears after the smaller number
	def MaxDiff(self, arr):
		small = float('inf')
		large = float('-inf')
		large_idx = len(arr)
		max_diff = float('-inf')
		for i in range(len(arr)):
			if arr[i] < small :
				if i > large_idx:
					max_diff = large-small
					large = arr[i]
				small = arr[i]
			if arr[i] > large:
				large = arr[i]
				large_idx = i
			if large-small > max_diff:
				max_diff = large-small
		return max_diff

	def maxDiff(self,arr, arr_size):
		max_diff = arr[1] - arr[0]
		min_element = arr[0]

		for i in range( 1, arr_size ):
			if (arr[i] - min_element > max_diff):
				max_diff = arr[i] - min_element

			if (arr[i] < min_element):
				min_element = arr[i]
		return max_diff

	def maxDist(self, arr):
		n = len(arr)

		max_dist = -1
		for i in range(len(arr)):
			j = n-1
			while (j > i):
				if arr[j] > arr[i] and max_dist < j-i:
					max_dist = j-i
				j = j-1
		return max_dist

	#find triplet
	def TwoSum(self,arr, target):
		store = dict()
		for i,v in enumerate(arr):
			if store.get(v):
				return v, target-v
			else:
				store[target-v] = v
		return None, None


	def Triplet(self, arr, target = 0):
		triple_list = []
		arr = sorted(arr)
		for i in range(len(arr)):
			one, two = self.TwoSum(arr ,target-arr[i])
			#print(one, two)
			if one and two:
				list_ = sorted([arr[i], one, two])
				if list_ not in triple_list:
					triple_list.append(list_)

		print(triple_list)
	# Trapping water
	def trap(self, height):
		large = 0
		trap = []
		store = dict()

		for i in arr:
			if i in store:
				store[i] = store[i] + 1
			else:
				store[i] = 1

		for idx, i in enumerate(height):
			if i >= large:
				if idx != len(height)-1:
					if max(height[idx-len(height)+1:]) >= i:
						#if current i is the only max after the index then max remains unchanged
						large=i


			diff = large - i

			trap.append(diff)

		ans = 0
		for i in trap:
			if i > 0:
				ans = ans + i
		if trap[-1] >= 0 and trap[-2] >= 0 and trap[-1] >= trap[-2]:
			ans = ans - trap[-1] -trap[-2]
		if trap[0] >= 0 and trap[1] >= 0 and trap[0] >= trap[1]:
			ans = ans - trap[1]- trap[0]

		return ans

	def ReverseArray(self, arr):
		length = len(arr)-1
		for i in range(int(len(arr)/2)):
			j = length - i
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
		return arr

	def SortColor(self, nums):
		i = 0
		j = len(nums)-1
		while i < j:
			if nums[i] != 0:
				if nums[j] == 0:
					nums[j], nums[i] = nums[i], nums[j]
					j= j-1
					i=i + 1
				elif nums[j] != 0:
					j = j-1
			elif nums[i] == 0:
				i = i + 1
		return nums

	def removeDuplicates(self, nums):
		i = 0
		j = 1
		prev = nums[i]
		curr = nums[j]
		while 1:
			if len(nums) == j:
				break
			if nums[i] == nums[j]:
				nums[j] = None
				j = j+1
			elif nums[i] != nums[j] and nums[i+1] == None:
				nums[i+1] = nums[j]
				i = i+1
			else:
				i = i+1
				j = j+1
		return nums, len(nums[:i+1])

	def BuySell(self, nums):
		max_profit = 0
		small = float('inf')
		for i in range(len(nums)-1):
			if nums[i] <= small:
				small = nums[i]
			if nums[i+1] - small > 0 and nums[i+1] - small > max_profit:
				max_profit = nums[i+1] - small
		return max_profit

	def MaxProdSub(self, nums):
		global_max = float('-inf')
		prod_sofar = 1
		for i in range(len(nums)):
			prod_sofar = prod_sofar * nums[i]
			if prod_sofar > global_max:
				global_max = prod_sofar
			if prod_sofar < 0:
				if nums[i+1] > 0:
					prod_sofar = 1
		return global_max
	def SortSquare(self, A):
		for idx, ele in enumerate(A):
			if ele >= 0:
				pos = idx
				break
		sorted_arr = []
		if  A[0] < 0 and A[-1] < 0:
			for k in reversed(A):
				sorted_arr.append(k**2)
			return sorted_arr

		if A[0] >= 0 and A[-1] >= 0:
			for k in A:
				sorted_arr.append(k**2)
			return sorted_arr

		j = pos-1
		i = pos
		while 1:
		#for _ in range(len(A)):
			#print(i,j)

			if j == -1:
				for k in A[i:]:
					sorted_arr.append(k**2)
				return sorted_arr
			if i == len(A):
				for k in reversed(A[:j+1]):
					sorted_arr.append(k**2)
				return sorted_arr

			if A[i] >= abs(A[j]):
				sorted_arr.append(A[j]**2)
				j = j-1

			elif abs(A[j]) > A[i]:
				sorted_arr.append(A[i]**2)
				i = i+1


		#return sorted_arr
	def SubArraySumK(self, nums, target):
		j = 0
		i = 0
		curr_sum = 0
		subArr_list = []
		while j != len(nums)-1:
			if curr_sum != target:
				curr_sum = curr_sum + nums[i]
				if i < len(nums)-1:
					i = i+1

			elif curr_sum == target:
				subArr_list.append([j,i])
				curr_sum = curr_sum - nums[j]
				j = j+1
	def MoveZeros(self, nums):
		i = 0
		j = 0
		while j != len(nums):
			if i == len(nums):
				break
			if i<j and nums[i]==0:
				if nums[j] != 0:
					nums[i], nums[j] = nums[j], nums[i]
				else:
					j = j+1
			else:
				i = i+1
		return nums

	def BinarySearchIter(self,nums, target):
		start = 0
		end = len(nums)-1
		while end <= start:
			mid = (start+end)//2
			if start == mid and nums[mid] == target:
				return mid
			elif nums[end] == target:
				return end

			if nums[mid] > target:
				start = start
				end = mid
			elif nums[mid] < target:
				start = mid
				end = end
			else:
				return mid

	def Mountain(self, A):
		i = 0
		global_max = 0
		count = 1
		flag_l = False
		flag_r = False
		if len(A) < 3 or A == []:
			return 0
		elif len(A) == 3 :
			if A[0] < A[1] > A[2]:
				return 3
			else:
				return 0
		while i < len(A)-1:

			if A[i] >= A[i+1]:
				i = i+1
			else:
				j = i
				while A[i] < A[i+1]  and i < len(A)-2:
					i = i+1
					flag_l = True

				if i == len(A)-2:
					return 0

				while A[i] > A[i+1]  and i < len(A)-2:
					i = i+1
					flag_r = True

				if i == len(A)-2 and A[i] > A[i+1]:
					i = i + 1
				if flag_l == flag_r:
					global_max = max(global_max, i-j+1)
				i = i+1

		return global_max





	def Mountain_neat(self, A):
		i = 0
		j = i
		global_max = 0

		while i < len(A)-1:
			if A[i] >= A[i+1]:
				i = i+1
			else:
				j = i
				flag_left = False
				flag_right = False
				while A[i] < A[i+1] and i < len(A)-2:
					i = i+1
					flag_left = True
				if i >= len(A)-1:
					return global_max
				while A[i] > A[i+1] and i < len(A)-2:
					i = i+1
					flag_right = True
				if i == len(A)-2 and A[i] > A[i+1]:
					i = i+1
					flag_right = True
				if flag_left == flag_right == True:
					global_max = max(global_max, i-j+1)
				if flag_right == False:
					i=i+1
		return global_max



	def SubArrayMinSize(self, nums, s):
		i = 0
		j = 0
		sum_here = 0
		sum_sofar = nums[i]
		min_length = float('inf')
		while i != len(nums)-1:
			if j <= len(nums)-1:
				if nums[j] >= s:
					return 1

			if sum_here < s and j < len(nums):
				sum_here = sum_here + nums[j]
				j = j+1
			elif sum_here >= s:
				min_length = min(j-i, min_length)
				sum_here = sum_here - nums[i]
				i = i+1
			else:
				i = i+1
		if min_length == float('inf'):
			return 0
		return min_length
	def summaryRanges(self, nums):
		i = 0
		j = 0
		string = []
		if nums == []:
			return []
		if len(nums) == 1:
			return [str(num[0])]
		while 1:
			if nums[j+1]-nums[j] == 1 or nums[j+1]-nums[j] == 0:
				j = j+1
				if j == len(nums)-1 and i != j:
					string.append(str(nums[i])+ "->"+str(nums[j]))
					return string					
			else:
				if i!=j:
					string.append(str(nums[i])+ "->"+str(nums[j]))
				else:
					string.append(str(nums[i]))
				i = j+1
				j = j+1
				if i == len(nums)-1:
					string.append(str(nums[i]))
					return string
		return string
	def SubarrayWithEqualZeros(self, nums):
		store = dict()
		add = 0
		maxLen = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				add = add - 1
			elif nums[i] == 1:
				add = add + 1
			if add == 0:
				maxLen = max(i+1, maxLen)
				
			if add not in store:
				store[add] = i
			
			else:
				maxLen = max(i-store[add], maxLen)
		return maxLen
		
			
	def BinarySearch(self, nums, target, flag):
		l = 0
		r = len(nums)-1
		mid = (l+r)//2
		res = -1
		while l <= r:
			mid = (l+r)//2
			if nums[mid] == target:
				res = mid
				if flag == 'r':
					r = mid - 1
				if flag == 'l':
					l = mid + 1
			elif nums[mid] > target:
				r = mid - 1
			else:
				l = mid + 1
		return res
	
	def removeElement(self, nums, val): #[0,1,2,2,3,0,4,2]
		i = 0
		j = len(nums)-1
		if len(nums)*[val] == nums:
			return 0
		while i<=j:
			if nums[j] == val:
				j = j - 1
			if i< len(nums) and nums[i] == val:
				nums[i], nums[j] = nums[j], nums[i]
				i = i + 1
				j = j - 1
			elif i < len(nums):
				i = i + 1
		return i
	def removeDuplicates2(self, nums):
		count = 0
		for i in range(len(nums)-1):
			if nums[i] == nums[i+1] :
				if count == 0:
					count = count + 1
				else:
					nums[i] = None
			elif nums[i] != nums[i+1]:
				count = 0
		i = 0 
		j = len(nums)-1
		while i < j:
			while nums[j] == None:
				j = j - 1
			if nums[i] != None:
				i = i + 1
			else:
				nums[i], nums[j] = nums[j], nums[i]
				i = i + 1
				j = j - 1 
		return i+1
	def RemoveDuplicates_(self, nums):
		i = 0
		j = 1
		count = 0
		length = len(nums)-1
		while  j < length:
			if nums[i] == nums[j] :
				if count == 0:
					count = 1
					i = i+1
					j = j+1
				else:
					nums.pop(j)
					length = length - 1
			else:
				count = 0
				i = j
				j = j+1
		return nums
	
	def power(x,n):
		if n == 1:
			return 1
		if n%2 == 0:
			y = power(x, n/2)
			return y*y
		else:
			return x * power(x,n-1)
		
			
				
			
				
		
				
#arr = [49 ,130, 124, 85, 455, 257, 341, 467, 377, 432, 309, 445, 440, 127, 324, 38, 39, 119, 83, 430, 42, 334 ,116, 140, 159, 205, 431, 478, 307, 174, 387, 22, 246, 425, 73, 271, 330, 278, 74, 98, 13, 487, 291, 162, 137, 356, 268, 156, 75, 32, 53, 351, 151, 442, 225, 467, 431, 108, 192, 8, 338, 458, 288, 254, 384, 446, 410, 210, 259, 222, 89 ,423, 447, 7, 31, 414, 169, 401, 92, 263, 156, 411, 360, 125, 38, 49, 484, 96, 42, 103, 351, 292, 337, 375 ]
#arr = [2,3,10,6,9,4,1,11]
#arr = [0, 0, 0, 0, 1, 1, 2, 1, 2, 2, 1, 1]
#arr = [12, 3, 4, 1, 6, 9]
#arr = [557,217, 627, 358, 527 ,358 ,338 ,272 ,870, 362, 897, 23, 618, 113, 718, 697, 586, 42, 424, 130, 230, 566, 560, 933]
#arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#arr = [2,0,1,3]
#arr = [3, 0, 0, 2, 0,0,1,0]
#arr = [0,0,0,0,1,0,0]

#nums = [7,6,4,3,1]
#nums = [1,1,2]

#print(arr)
nums = [2,1,4,7,3,2,5]
nums = [0,1,2,3,4,7,4,3,2,1,0,2,1,4,7,3,2,5]
nums = [0,1,2,4,5,7]
nums = [0,1,2,3]

nums = [10,2,-2,-20,10]
Arrays = Arrays(nums)

def power(x,n):
	res = 1
	if n == 0:
		return 1
	if n < 0:
		x = 1/x
		n = -1*n
	while n!=0:
		if n%2 == 0:
			x = x*x
			n =n//2
		else:
			res = x * res
			n = n-1
	return res
def divide(dividend, divisor):
	if dividend == 0 :
		return 0
	if dividend == -2147483648 and abs(divisor) == 1:
		return -2147483647*divisor
	elif abs(divisor) == 1:
		return dividend*divisor
	s = 0
	e = abs(dividend)-1
	res = 1
	while s<=e:
		mid = (s+e)//2
		if abs(divisor)*mid <= abs(dividend):
			res = mid
			s = mid+1
		elif abs(divisor)*mid > abs(dividend):
			e = mid-1
	
	if dividend*divisor<0:
		return res*-1
	else:
		return res
def search2d(matrix, target):
	if len(matrix[0]) == len(matrix) == 1:
		if matrix[0][0] == target:
			return True
		else:
			return False
	range_list = []
	for i in range(len(matrix)):
		range_list.append(matrix[i][0])
		range_list.append(matrix[i][-1])
	print(range_list)
	def binarysearch(nums, target):
		start = 0 
		end = len(nums)-1
		res = -1
		while start <= end:
			mid = (start+end)//2
			if nums[mid] < target:
				start = mid+1
			elif nums[mid] == target:
				return mid, True
			else:
				end = mid-1
		
		return start-1, False
	idx,flag = binarysearch(range_list, target)
	if flag:
		return True
	else:
		row = idx//2
		row_search, flag = binarysearch(matrix[row], target)
		if flag:
			return True
		else:
			return False
		
def findPeak(nums):
	start = 0
	end = len(nums)-1
	while start<end:
		mid = (start+end)//2
		if nums[mid]>nums[mid+1]:
			end = mid
		else:
			start = mid+1
	return end

def bsGreaterLesser(nums, target):
	start, low = 0,0
	end = len(nums)-1
	high = end
	while start<end:
		mid = (start+end)//2
		if nums[mid] < target:
			low = mid
			start = mid+1
		elif nums[mid] > target:
			high = mid
			end = mid-1
		else:
			if mid == len(nums)-1:
				return low, end
			else:
				return start, high
			
	return low, high
def searchRotatedArr(nums, target):
	start = 0
	end = len(nums)-1
	pivot = None
	while start<=end:
		mid = (start+end)//2
		if nums[mid] < nums[mid-1]:
			pivot = mid
			break
		elif nums[0] <= nums[mid]:
			start = mid+1
		elif nums[0] > nums[mid]:
			end = mid-1
	def binarySearch(nums, target):
		start = 0
		end = len(nums)-1
		while start<=end:
			mid = (start+end)//2
			if nums[mid] == target:
				return True
			elif nums[mid] < target:
				start = mid+1
			elif nums[mid] > target:
				end = mid-1
		return False
	if pivot != None and binarySearch(nums[:pivot], target):
		return True
	elif pivot != None and not binarySearch(nums[:pivot], target):
		return binarySearch(nums[pivot:], target)
	else:
		return False
		
	
		
		
#func = divide(-2147483648,-1)

#matrix = [
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
#]
nums = [2,2,2,0,2,2]
func = searchRotatedArr(nums, 3)
#end = Arrays.BinarySearch(nums, target, 'l')
#end = Arrays.BinarySearch(nums, target+1)
print(func)

