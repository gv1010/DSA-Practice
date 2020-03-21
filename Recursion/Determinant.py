def determinant(A):
	if len(A) == 2 and len(A[0]) == 2:
		return A[0][0]*A[1][1] - A[1][0]*A[0][1]
	new = []
	total = []
	for i, num in enumerate(A[0]):
		for j in range(1,len(A[0])):
			new.append(A[j][:i] + A[j][i+1:])
		cofactor = determinant(new)
		total.append(((-1)**i )*A[0][i]*cofactor)
		print(total)
		new = []
	return sum(total)
A = [[1,2,3],[1,2,3],[1,2,3]]
#A = [[1,0,0],[0,1,0],[0,0,1]]
#A = [[1,2,3,4],[4,3,2,1],[2,3,4,1],[4,2,4,1]]
print(determinant(A))
			