def rotation(arr, k):
	if k > len(arr):
		print(k%len(arr))
		k = (k%len(arr))
	print(k)
	start = 0
	end = len(arr)
	
	reverse(arr, start, end-k-1)
	print(arr)
	reverse(arr, end-k, end-1 )
	print(arr)
	reverse(arr, start, end-1)
	
	def reverse(arr, start, end):
		while start< end:
			arr[start], arr[end] = arr[end], arr[start]
			start = start + 1
			end = end - 1
		return arr
	arr = [1,2,3,4,5,6,7]
	start = 0
	end = len(arr)
	(rotation(arr, k = 10))
	print(arr)
#print(reverse(arr, start=0, end=len(arr)-1))

def func(arr, start , end, target):
	if arr == []:
		return -1
	if arr[0] < arr[-1]:
			return bst(arr, 0, len(arr)-1, target)
	while 1:
		pivot = int((start+end)/2 )
		
		if arr[pivot] == target:
			return pivot
		if arr[start] == target:
			return start
		if arr[end] == target:
			return end
			
		if arr[pivot] > arr[pivot + 1]:
			pivot = pivot + 1
			end = len(arr)-1
			
			if arr[pivot] < target < arr[end]:
				return bst(arr, pivot, end, target)
			elif arr[pivot] > target > arr[end]:
				return bst(arr, 0, pivot-1, target)
			else:
				return -1
			
		else:
			if arr[pivot] > arr[start]:
				#func(arr, pivot+1, end)
				start = pivot + 1
				end = end
			else:
				#func(arr, start, pivot)
				start = start 
				end = pivot
	#return pivot
	


def bst(arr, start, end, target):

	while 1:
		
		pivot = int((start+end)/2)
		if start==end and arr[pivot] == target:
			return pivot
		elif start == end and arr[pivot] != target:
			return -1
		if target <= arr[pivot]:
			start = 0
			end = pivot
		else:
			start = pivot+1
			end = end
			
#arr = []
arr = [4,5,6,7,0,1,2,3, ] 
target = 0
start = 0
end = len(arr)-1
#print(bst(arr, start,end, target))
print(func(arr, start, end, target))
	
	
	
	
