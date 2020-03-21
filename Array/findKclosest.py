def findkclosest(nums, k, x ):
	start = 0
	end = len(nums)-1
	target_mid = None
	res = None
	while start<=end:
		mid = (start+end)//2
		if nums[mid] == x:
			res = mid
			break
		if nums[mid] < x :
			res = mid
			start = mid + 1
		else:
			res = mid
			end = mid - 1
	return res
	
	
from collections import defaultdict

def groupAnagrams(strs):
	store = dict()
	for st in strs:
		ele = "".join((sorted(st)))
		st = str(st)
		if ele in store:
			store[ele] = store[ele]+[st]
		else:
			store[ele] = [st]
		#print(store)
	#return store
	return list(store.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]   
nums = [1,2,4,5,7]
k=4
x=6
#print(strs[1])
print(groupAnagrams(strs))