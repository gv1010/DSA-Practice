def permute(A, P):
	for i in range(len(A)):
		while P[i] > 0:
			temp = A[P[i]]
			A[P[i]] = A[i]
			new_idx = P[i]
			A[P[i]] = temp
			P[i] = -1


A = ['a','b','c','d']
P = [2,3,0,1]