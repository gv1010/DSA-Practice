def rod(arr, n,cache):
	if n == 0:
		return 0
	k=n//2
	max_result = float('-inf')
	if cache[n] != -1:
		return cache[n]
	for i in range(1,k+1):
		result = rod(arr,n-i,cache) + rod(arr, i,cache)
		max_result = max(result,max_result)
	max_result = max(max_result, arr[n])
	cache[n] = max_result 
	return cache[n]
	

#iter = int(input())
#for i in range(iter):
#	n = int(input())
#	cache=[-1]*(n+1)
#	l = list(map(int,input().split()))
#	l.insert(0,0)
#	print(l,n)
#	print(rod(l,n,cache))
#	print()
#	
arr = [0, 6, 15, 8, 9, 10, 17, 17, 20, 1, 5, 8, 9, 10, 17, 17, 20]
n = 5
cache=[-1]*(n+1)

print(rod(arr,n, cache))
print(cache)