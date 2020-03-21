

def func(arr, start , end ):

	if len(arr) == 1:
		return 0
	pivot = (start + end) // 2
	
	if arr[pivot] > arr[pivot+1]:
		return pivot+1 
	elif start == end:
		#print(start, end)
		return -1
		
	if arr[pivot] > arr[end]:
		return func(arr, pivot, end)
	else:
		return func(arr, start, pivot)
		
def bst(arr, start, end, target):
	mid = (start + end) // 2
	#print(start, mid, end)
	if start == mid and arr[mid] != target and arr[end] != target:
		return False
	if start == mid and arr[end] == target:
		return end
	if arr[mid] == target:
		return mid
	if arr[mid] > target:
		return bst(arr, start, mid, target)
	elif  arr[mid] < target:
		return bst(arr, mid, end, target)
	
def drive():
	arr = [2,3]
	start = 0
	end = len(arr)-1
	target = 2
	pivot = func(arr, start , end )

	if pivot != -1:
		if arr[pivot] <= target <= arr[-1]:
			index = bst(arr, pivot, end, target)
			return index

		elif arr[0] <= target <= arr[pivot-1]:
			index = bst(arr, 0, pivot-1, target)
			return index
		else:
			return -1
	else:
		index = bst(arr, start, end, target)
		return index
arr = [1,3,5]
start = 0
end = len(arr)-1
target = 2
#pivot = func(arr, start , end )
print(func(arr, start , end ))		
#print(drive())

		
	