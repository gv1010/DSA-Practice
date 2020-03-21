def countingWays(M,N):
	if M == 1 or N == 1:
		return 1
	return countingWays(M-1, N) + countingWays(M, N-1)
M = 3
N = 3

print(countingWays(M,N))