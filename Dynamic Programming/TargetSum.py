from collections import defaultdict
#store_val = defaultdict(list)
store = defaultdict(dict)

	nums = [1,1,1]
def targetSum(nums, S, i):
	if i == len(nums):
		if S == 0:
			return 1
		else:
			return 0
	value = targetSum(S+nums[i], i+1) + targetSum(S-nums[i], i+1)
	value = store[i+1][S+nums[i]] + store[i+1][S-nums[i]]
	store[i][S]= value
	return store[i][S]
S = 3
print(targetSum(nums, S, 0))