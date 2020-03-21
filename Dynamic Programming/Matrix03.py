class DP:
	def __init__(self):	
		self.maxSize = float('-inf')
		self.arr = [
					[0,1,1,1],
					[0,0,1,1],
					[0,1,1,1],
					[1,1,1,1]
					]
	def matrixDP(self, matrix, i, j):
	for i in range
		if i == len(matrix)-1 or j == len(matrix[0])-1 :
			return matrix[i][j]
		elif matrix[i][j] == 1 and i< len(matrix)-1 and j<len(matrix[0])-1:
			self.arr[i][j] = 1 + min(self.arr[i+1][j], self.arr[i][j+1], self.arr[i+1][j+1])
		elif matrix[i][j] == 0 and i< len(matrix)-1 and j<len(matrix[0])-1:
			self.arr[i][j] = min(self.arr[i+1][j], self.arr[i][j+1], self.arr[i+1][j+1])
		self.maxSize = max(self.arr[i][j], self.maxSize)
		return self.arr[i][j]
	def printOpt(self):
		print(self.maxSize)
		print(self.arr)



matrix = [
  [0,1,1,1],
  [0,0,1,1],
  [0,1,1,1],
  [1,1,1,1]
]
#matrix = [[1,1,1,0],[1,1,1,0],[1,1,1,1]]
i = 0 
j = 0
d = DP()

print(d.matrixDP(matrix, i,j))
print(d.printOpt())