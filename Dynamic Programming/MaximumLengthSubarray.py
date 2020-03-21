def maximum(m,n):
	arr = [[0 for i in range(len(m)+1)] for j in range(len(n)+1)]
	max_sub = float('-inf')
	for i in range(0,len(m)+1):
		for j in range(0, len(n)+1):
			if i==0 or j==0:
				arr[i][j] = 0
			elif  m[i-1] == n[j-1]:
				arr[i][j] = 1 + arr[i-1][j-1]
				max_sub = max(max_sub, arr[i][j])
	return max_sub
			
m = [1,3,2,1,2]
n = [3,2,1,2,7]
print(maximum(m,n))