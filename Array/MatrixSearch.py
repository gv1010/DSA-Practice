def matrixfind(matrix, target):
	for i in range(len(matrix)):
		if matrix[i][0] <= target <=matrix[i][-1]:
			start = 0
			end = len(matrix[i])-1
			while start <= end:
				mid = (start+end)//2
				if matrix[i][midn] == target:
					return True
				elif matrix[i][mid] < target:
					start = mid+1
				else:
					end = mid-1
	return False
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 55
print(matrixfind(matrix, target))