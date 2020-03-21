
def twosum(arr, target):
	dict  = {}
	for i in range(0,len(arr)):
		if arr[i] in dict.values():
			return dict
				
		else:
			dict[arr[i]] = target - arr[i]
			

arr = [2,5,3,4,8]
print(twosum(arr,7))