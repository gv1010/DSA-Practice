w = [0,10, 20, 30]
v = [0,100, 80, 150]
W = 50

cache = []
def knapsack(W,i,w, cache):
	
	if i == len(w)-1:
		return 0
	if W-w[i] < 0:
		return knapsack(W,i+1,w,cache)
	value = max(knapsack(W-w[i],i+1,w,cache) + v[i], knapsack(W,i+1,w,cache))
	cache.append(value)
	return value
#print(knapsack(W,0,w, cache))
#print(cache)
def knapsackDPI(W,v,w):
	cache = [[0]*(W+1) for i in range(len(v))]
	for i in range(len(w)):
		for j in range(W+1):
			if i == 0 or j == 0:
				cache[i][j] = 0
			elif w[i] > j:
				cache[i][j] = cache[i-1][j]
			else:
				cache[i][j] = max(v[i]+cache[i-1][j - w[i]], cache[i-1][j])
	return cache[len(v)-1][W]
	
print(knapsackDPI(W,v,w))