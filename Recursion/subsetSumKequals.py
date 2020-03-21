class Subset:
	def subsetSum(self, nums, k):
		if sum1%k != 0:
		sum1 = sum(nums)
			return False
		target = sum1//k 
		length = len(nums)
		def canPart(target, path, res, i):
			if target == 0 and sorted(path) not in res:
				return res.append(sorted(path))
			if i == length:
				if target != 0:
					return 
				else:
					return res.append(path)
			
			canPart(target-nums[i], path+[nums[i]], res, i+1)
			canPart(target, path, res, i+1)
			
		path = []
		i = 0
		res = []
		canPart(target, path, res, i)
		return res
s = Subset()
nums = [4,2,3,2,3,1,5]
k = 4
print(s.subsetSum(nums, k))
	