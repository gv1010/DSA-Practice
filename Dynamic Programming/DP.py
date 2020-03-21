
def fib(n):
	fib_d = dict()
	fib_d[0] = 1
	fib_d[1] = 1
	for i in range(n):
		if i not in fib_d:
			fib_d[i] = fib_d[i-1] + fib_d[i-2]
	return fib_d[n-1]

def ugly(n):
	i = 1
	count = 1
	value = []
	if n <= 10:
		return n
		
	while count <= n+1:
		
		if i>=1 and i <= 10:
			value.append(i)
			count = count + 1
		elif (i%2 == 0 and i%3 == 0 and i%5 != 0) or (i%2 != 0 and i%3 == 0 and i%5 == 0) or (i%2 == 0 and i%3 != 0 and i%5 == 0):
			value.append(i)
			count = count + 1
		i = i+1
	return value[-1]

#def MakeChange(value):
#		#print(minCoins[0])
#		nonlocal coins_dict
#		minCoins = float('inf')
#		if value == 0:
#			return 0
#		#print(coins_dict)
#		for i in coins:
#			#print(value-i)
#			if (value-i >= 0):
#				
#				if value-i not in coins_dict.values():
#					coins_dict[value-i] = MakeChange(value - i)
#					if (coins_dict[value-i] <= minCoins):
#						minCoins = coins_dict[value-i]
#				else:
#					coins_count = coins_dict[value - i]
#					if (coins_count <= minCoins):
#						minCoins = coins_count
#		return minCoins + 1
import time

def MainFunc(value, coins):
	minCoins = float('inf')
	coins = coins
	coins_dict = dict()
	def MakeChange_recursion(value):
		#print(minCoins[0])
		minCoins = float('inf')
		if value == 0:
			return 0
		#print(coins_dict)
		for i in coins:
			#print(value-i)
			if (value-i >= 0):
				
				#if value-i not in coins_dict.values():
				#	coins_dict[value-i] = MakeChange(value - i)
				#	if (coins_dict[value-i] <= minCoins):
				#		minCoins = coins_dict[value-i]
				#else:
				coins_count = MakeChange_recursion(value - i)
				if (coins_count <= minCoins):
					minCoins = coins_count
		return minCoins + 1
	#print(MakeChange_recursion(value))
	def MakeChange(value):
		#print(minCoins[0])
		nonlocal coins_dict
		minCoins = float('inf')
		if value == 0:
			return 0
		#print(coins_dict)
		for i in coins:
			#print(value-i)
			if (value-i >= 0):
				
				if value-i not in coins_dict.values():
					coins_dict[value-i] = MakeChange(value - i)
					if (coins_dict[value-i] <= minCoins):
						minCoins = coins_dict[value-i]
				else:
					coins_count = coins_dict[value - i]
					if (coins_count <= minCoins):
						minCoins = coins_count
		return minCoins + 1
	#print(MakeChange(value))
	def MakeChange_bottomUP(value):
		coins_dict[0] = 0
		coins_dict[1] = 1
		for i in range(1, value+1):
			minCoins = float('inf')
			for coin in coins:
				if i-coin>=0:
					count_coins = coins_dict[i-coin]+1
					if count_coins <= minCoins:
						minCoins = count_coins
			coins_dict[i] = minCoins
		return coins_dict[value]
	print(MakeChange_bottomUP(value))
value = 99
coins = [10,5,1]
start_time = time.time()
(MainFunc(value, coins))
print(time.time() - start_time)


