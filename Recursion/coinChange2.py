def coinChange(amount, coins):
	if len(coins) == 0 or amount == 0 or amount < min(coins):
		if amount == 0:
			return 1
		else:
			return 0
	count = 0
	for i in range(len(coins)):
		if amount >= coins[i]:
			count = count+coinChange(amount-coins[i], coins[i:])
	return count
amount = 500
coins = [3,5,7,8,9,10,11]
#print(coinChange(amount, coins))

def coinIter(amount, coins):
	import copy
	dp = [1]+[0]*(amount)
	k = 0
	length = [len(coins)]
	for i in range(length[0]):
		dp1 = [1]+[0]*(amount)
		print(1)
		for j in range(1,amount+1):
			if j >= coins[i]:
				dp1[j] = dp1[j] + dp[j-coins[i]]
		print(dp1)
		dp = copy.copy(dp1)
		k = k+1
		length =  [len(coins[k:])]
	return dp[amount]

amount = 5
coins = [1,2,5]
print(coinIter(amount, coins))

