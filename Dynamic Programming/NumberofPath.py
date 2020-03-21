def path():
	matrix = [[0,0,0],
			[0,1,0],
			[0,0,0]]
	m = len(matrix)
	n = len(matrix[0])
	for j in range(n):
		A[0][j] = 1
	for i in range(m):
		A[i][0] = 1
		
	for i in range(1,m):
		for j in range(1,n):
			if matrix[i][j] != 1:
				A[i][j] = A[i-1][j]+A[i][j-1]
			else:
				A[i][j] = 0
				
	return A[m-1][n-1]
def matrix(l,w):
	
	A = [[0]*w for j in range(l)]
	return A
	
A = matrix(3,3)

print(path())

	