def maxCoins(matrix):
	import copy
	dp = copy.deepcopy(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i == 0 and j >= 1:
				dp[i][j] = matrix[i][j] + dp[i][j-1]
			elif j == 0 and i >= 1:

				dp[i][j] = matrix[i][j] + dp[i-1][j]
			elif i!=0 and j !=0:
				dp[i][j] = max(matrix[i][j]+dp[i-1][j],matrix[i][j]+dp[i][j-1])
	print(dp)
	return dp[len(matrix)-1][len(matrix[0])-1]
	
matrix = [[0,3,1,1],
		  [2,0,0,4],
		  [2,5,3,1]]
		  
print(maxCoins(matrix))