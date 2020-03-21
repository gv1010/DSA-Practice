def minSingle(num, cache):
	if num == 0:
		return 0
	if cache[num] != -1:
		return cache[num]
	loop_min = float('inf')
	curr_min = 0
	for i in [2,5]:
		if num-i >= 0 :
			curr_min = minSingle(num-i,cache)
			if curr_min < loop_min:
				loop_min = curr_min
	loop_min = loop_min + 1
	cache[num] = loop_min
	return cache[num]
	
def coinChange(coins, amount):
	cache = [-1]*(amount+1)
	cache[0] = 0
	for j in range(1, amount+1):
		loop_min = float('inf')
		for i in coins:
			if j-i >= 0:
				min_coin = cache[j-i] + 1
				if min_coin < loop_min:
					loop_min = min_coin
		cache[j] = loop_min
	print(cache)
	if cache[amount] != float('inf'):
		return cache[amount]
	else:
		return -1
		
	
coins = [3,2,5]
amount = 11
print()
print(coinChange(coins, amount))	
	
#num = 11
#cache = [-1]*(num+1)
#print(minSingle(num, cache))
#print(cache)