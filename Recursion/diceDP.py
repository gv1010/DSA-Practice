'''crux is '''
def dice(d, f, target):
	prev = [1]+[0]*(target)
	for dice in range(1, d+1):
		dp = [0]*(target+1)
		for i in range(1, target+1):
			if i >= dice:
				for face in range(1, f+1):
					if i >= face:
						dp[i] = dp[i]  + prev[i-face]
						dp[i] = dp[i] 
					
						
		prev = dp
	return (dp[target])% (1000000007)
	
print(dice(30,30, 500))