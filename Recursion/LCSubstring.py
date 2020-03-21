class LCS:
	def __init__(self, s1, s2):
		self.count = 0
		self.s1 = s1
		self.s2 = s2
	def lcs(self):
		
		c = len(self.s2)
		r = len(self.s1)
		arr = [[0]*(c) for j in range(r)]
		result = float('-inf')
		for i in range(r):
			for j in range(c):
				if (i == 0 or j == 0) and self.s1[i] == self.s2[j]:
					arr[i][j] = 1
					result = max(result, arr[i][j])
				elif self.s1[i] == self.s2[j] :
					arr[i][j] = 1 + arr[i-1][j-1]
					result = max(result, arr[i][j])
					#arr[i][j] = max(arr[i-1][j], arr[i][j-1])
				else:
					arr[i][j] = 0
		#print()
		print(arr)
		return (result)
		 
s1 = "abcd"
s2 = "abcde"



l = LCS(s1, s2)
print(l.lcs())