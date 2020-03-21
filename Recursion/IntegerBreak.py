def breakInteger(n):
	cache = [1]*(n+1)	
	for i in range(2, n+1):
		val = -1
		for j in range(1,i//2+1 ):
			val = max(j*cache[i-j], j*(i-j), val)
		cache[i] = val
	return cache[n]
def recursionIB(n, dp):
	if n == 0 or n==1 :
		return 1
	res = 1
	if dp[n]:
		return dp[n]
	for i in range(1,n+1):
		res = max(i * recursionIB(n-i,dp), res) #i*(n-i))
		#print(i,res)
	dp[n] = res
	print(dp)
	return res
n = 58
dp = [0]*(n+1)
print('for n = ', n)
print(dp)
print('integer break is = ',recursionIB(n, dp))