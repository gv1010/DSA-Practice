def kthsmallest(matrix, k):
	import heapq
	arr = []
	for i in range(len(matrix[0])):
		arr.append((matrix[0][i], 0, i))
	heapq.heapify(arr)
	for _ in range(k-1):
		tup = heapq.heappop(arr)
		x, y = tup[1], tup[2]
		if x+1 < len(matrix):
			heapq.heappush(arr,(matrix[x+1][y], x+1, y))
	return heapq.heappop(arr)[0]
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(kthsmallest(matrix, k))
			