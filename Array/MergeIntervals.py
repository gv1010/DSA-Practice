def mergeIntervals(matrix):
	matrix.sort(key = lambda x: x[0])
	result = []
	length = len(matrix)
	for interval in matrix:
		if result == [] or result[-1][1] < interval[0]:
			result.append(interval)
		else:
			result[-1][1] = max(result[-1][1], interval[1])

	return result
	
	
def sqrt(num):
	if num == 0 or num == 1:
		return num
	start = 0
	end = num-1
	mid = 0
	
	while start<=end:
		
		#print(start, end, mid)
		mid = (start+end)//2
		if mid*mid > num:
			end = mid-1
		elif mid*mid < num:
			res = mid
			start = mid+1
		else:
			return mid

	return res
	
print('s','e', 'm', end = "")
print()
print(sqrt(1023))
#matrix = [[2,3],[4,5],[7,10],[9,17]]
#res = mergeIntervals(matrix)
#print(res)
#print(mergeIntervals(res))