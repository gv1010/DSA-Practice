class MinPathSum:
	def __init__(self):
		self.global_min = float('-inf')
	min_path = float('inf')
	def minPath__(self, matrix):
		arr = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix)) ]
		arr[0][0] = 0
		val = [0] * len(matrix)
		for x in range (len(matrix)):
			val[x] = [0] * len(matrix[0])
		print(val)
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if i == 0 and j == 0:
					arr[i][j] = min(matrix[i][j], matrix[i][j])
				elif i == 0 :
					arr[i][j] = min(matrix[i][j] + arr[i][j-1], matrix[i][j] + arr[i][j-1])
				elif j == 0:
					arr[i][j] = min(matrix[i][j] + arr[i-1][j], matrix[i][j] + arr[i-1][j])
				else :
					arr[i][j] = min(matrix[i][j] + arr[i-1][j], matrix[i][j] + arr[i][j-1])		
		print(arr)	
				
	def minPath(self,matrix, i, j, sum_path):
		print(i,j)
		if i == 0 and j == 0:
			self.min_path = min(self.min_path, sum_path+matrix[i][j])
			return
		if i >= 0:
			self.minPath(matrix, i-1, j, sum_path + matrix[i][j])
		if j >= 0:
			self.minPath(matrix, i, j-1, sum_path + matrix[i][j])
		return self.min_path
matrix = [[1,3,1],[1,5,1],[4,2,1]]
#matrix = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
i = 2
j = 2
sum_path = 0
f = MinPathSum()

print(f.minPath__(matrix))
