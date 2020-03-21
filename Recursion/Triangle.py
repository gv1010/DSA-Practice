def triangle1(triangle):
	prev = triangle[-1]
	new = []
	for A in reversed(triangle[:len(triangle)-1]):
		new = []
		for k in range(len(A)):
			new.append(min(prev[k] + A[k], prev[k+1] + A[k]))	
		prev = new	
	return prev[0]
	
A = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
A = [[-1],[2,3],[1,-1,-3]]
print(triangle1(A))