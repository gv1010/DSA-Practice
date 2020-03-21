#
#def twoSum(nums, target) :
#	store = dict()
#	search = dict()
#	for i, j  in enumerate(nums):
#		store[j] = i
#	for i in nums:
#		rem = target-i
#		if store.get(rem):
#			return [store[i], store[rem]]
#		
#
#arra = [2,5,7,11]
#target = 9
#out = twoSum(arra,target)
#print(out) 
import time 
def twoSum(nums, target) :
	search = {}
	start = time.time()
	for i,v in enumerate(nums):
		num = target - nums[i]
		#if search.get(num):
		if num in search.keys():
			print(num)
			return [i, search[num]]
		else:
			search[v] = i
	
arr = [3,7,2,1]
target = 9
start = time.time()
print(twoSum(arr, target))
print(time.time()-start)


#def twoSum(arr, target):
#
#	search = dict()
#	for i,v in enumerate(arr):
#		num = target - arr[i]
#		if num in search.keys():
#			print(i, search[num])
#		else:
#			search[v] = i
#		
