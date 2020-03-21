def setzero(matrix):
	row_set = set()
	col_set = set()
	for i in range(1,len(matrix)):
		for j in range(1,len(matrix[0])):
			if matrix[i][j] == 0:
				matrix[i][0] = 0
				matrix[0][j] = 0
	print(matrix)
	#for i in range(len(matrix)):
	#	for j in range(len(matrix[0])): 
	#		if not matrix[i][0] or not matrix[0][i] :
	#			matrix[i][j] = 0
	#		
	
	
	
	
	for i in range(1,len(matrix)):
		if matrix[i][0] == 0:
			for j in range(len(matrix[0])):
				if j!=0:
					matrix[i][j] = 0
	for j in range(1,len(matrix[0])):
		if matrix[0][j] == 0:
			for i in range(len(matrix)):
				if not(i==j== 0):
					matrix[i][j] = 0
	if matrix[0][0] == 0:
		for i in range(len(matrix)):
			matrix[i][0] = 0
		for j in range(len(matrix[0])):
			matrix[0][j] = 0
	return matrix

matrix = [
  [1,1,2,1],
  [1,4,5,1],
  [1,3,0,5]
]
print(setzero(matrix))
				
	