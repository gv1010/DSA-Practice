def substring(s):
	i = 0
	j = 0
	store = []
	glb_max = 0
	for j in range(len(s)):
		if s[j] in store:
			idx= store.index(s[j])
			store = store[idx+1:]
			store.append(s[j])
			
		else:
			store.append(s[j])
	return len(store)
	
s = "abcddfhy"
print(substring(s))
			
	

2 Heaps
1. Find Median from Data Stream
2. Sliding Window Median
3. IPO
Session:
	