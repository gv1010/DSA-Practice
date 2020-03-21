def merge(intervals):
	intervals.sort(key = lambda x:x[0])
	result = []
	
	for interval in intervals:
		if result == [] or  result[-1][1] < interval[0]:
			result.append(interval)
		else:
			result[-1][1] = max(interval[1], result[-1][1])
	return result
			
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
"""Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}"""
intervals = [[0, 3], [2, 6], [3, 4], [6, 9]]

print(merge(intervals))
			
		