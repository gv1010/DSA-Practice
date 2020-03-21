def maxPath(A,i,j,dp):
	if dp[i][j] > -1:
		return dp[i][j]
	if (i-1>=0 and j-1 >= 0 and i+1 <= len(A)-1 and j+1 <= len(A[0])-1):
		if A[i][j] + 1 != A[i-1][j] and A[i][j] + 1 != A[i][j-1] and A[i][j] + 1 != A[i][j+1] and A[i][j] + 1 != A[i+1][j] :
			return 1
	count = 1
	if i-1>=0 and A[i][j] + 1 == A[i-1][j]:
		count = max(count,1 + maxPath(A, i-1, j,dp))
		
	if j-1>=0 and A[i][j] + 1 == A[i][j-1]:
		count = max(count,1 + maxPath(A, i, j-1,dp))
		
	if i+1 <= len(A)-1 and A[i][j] + 1 == A[i+1][j]:
		count = max(count,1 + maxPath(A, i+1, j,dp))
		
	if j+1 <= len(A[0])-1 and A[i][j] + 1 == A[i][j+1]:
		count = max(count,1 + maxPath(A, i, j+1,dp))
	
	dp[i][j] = count
	return count
def maxPathHelp(A):
	maxVal = float('-inf')
	dp = [[-1]*len(A[0]) for i in range(len(A))]
	for i in range(len(A)):
		for j in range(len(A[0])):
			val = maxPath(A, i, j, dp)
			maxVal = max(val, maxVal)
	print(dp)
	return maxVal
A = [[ 1, 2, 9], 
      [ 5, 3, 8], 
      [ 4, 6, 7]]
#print(maxPathHelp(A))