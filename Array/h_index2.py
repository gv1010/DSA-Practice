def hindex(citations):
	start = 0
	end = len(citations)-1
	while start <= end:
		idx = start + (end-start)//2
		if citations[idx] >= len(citations)-idx:
			end = idx-1
			result = len(citations)-idx
		else:
			start = idx + 1
	return result
	
citations = [0,1,3,5,6]
citations = [1,4,4,4,5,6,6]
print(hindex(citations))