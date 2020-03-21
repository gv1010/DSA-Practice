def ruleofLife(matrix):
	neighbour = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
	count = 0
	for p in range(len(matrix)):
		for q in range(len(matrix[0])):
			count = 0
			for i in range(p-1,p+2,1):
				for j in range(q-1,q+2,1):
					if 0<=i<=len(matrix)-1 and 0<=j<=len(matrix[0])-1:
						if(not(i==p) or not (j==q)) and matrix[i][j] == 1:
							count = count + 1
			neighbour[p][q] = count
			
			
	for p in range(len(matrix)):
		for q in range(len(matrix[0])):
			if matrix[p][q] == 1:
				if neighbour[p][q] < 2:
					matrix[p][q] = 0
				if neighbour[p][q] == 2 or neighbour[p][q] == 3:
					matrix[p][q]
				if neighbour[p][q] > 3:
					matrix[p][q] = 0
			else:
				if neighbour[p][q] == 3:
					matrix[p][q] = 1
	return matrix
	#return [count, 8-count]
					
matrix = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(ruleofLife(matrix))