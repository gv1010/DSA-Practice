def matrixBlock(mat, K):
	import copy
	buf = copy.deepcopy(mat)
	for i in range(1, len(mat)):
		for j in range(len(mat[0])):
			buf[i][j] = buf[i-1][j]+buf[i][j]
	answer = [[0]*len(mat[0]) for i in range(len(mat))]
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if i == len(mat)-1:
				if j-K >= 0:
					answer[i][j] = sum(buf[i][j-K:j+K+1])- sum(buf[i-K-1][j-K:j+K+1)
				else:
					answer[i][j] = sum(buf[i][:j+K+1]) - sum(buf[i-K-1][:j+K+1])
			elif i == 0:
				if j-K >= 0:
					answer[i][j] = sum(buf[i][j-K:j+K+1])
				else:
					answer[i][j] = sum(buf[i][:j+K+1
			elif i-K <:
				
	return buf
mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 1
print(matrixBlock(mat, K))