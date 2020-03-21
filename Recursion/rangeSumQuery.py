def rangeSum(matrix, row1,col1, row2, col2):
	import copy
	data = copy.copy(matrix)
	for i in range(len(data)):
		sum1 = 0
		for j in range(len(data[i])):
			sum1 = sum1 + data[i][j]
			data[i][j] = sum1
	sum2 = 0
	for j in range(row1, row2+1):
		sum2 = sum2 + data[j][col2] - data[j][col1-1]
	return sum2
	
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

#print(rangeSum(matrix, 2,1, 4, 3))
print(rangeSum(matrix, 1, 1, 2, 2))
			
