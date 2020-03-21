class Permutation:
	def __init__(self):
		self.result = []
	def permute(self,nums, i):
		if i == len(nums):
			return self.result.append(nums)
		for j in range(i,len(nums)):
			a = nums.copy()
			a[i], a[j] = a[j], a[i]
			self.permute(a,i+1)
		return self.result
		
p = Permutation()
per = [1,2,3]
print(p.permute(per,0))