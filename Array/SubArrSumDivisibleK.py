def subArr(A, K):
	from collections import defaultdict
	from collections import Counter
	arr = [0]
	val = 0
	count = 0
	store = defaultdict(int)
	for item in A:
		val = val + item
		arr.append(val%K)
		#store[val%K] = store[val%K]+1
	res = 0
	count = Counter(arr)
	return sum(v*(v-1)//2 for v in count.values())
	#for i in range(len(A)+1):
	#	for j in range(i+1,len(A)+1):
	#		if abs(arr[j]- arr[i])%K == 0:
	#			#print(i,'---',j)
	#			count = count + 1
	#return count
A = [4,5,0,-2,-3,1]
K = 5
#A = [1,2,3]
#K = 3
A = [5,5,5,5]
K = 5
print(subArr(A, K))
		