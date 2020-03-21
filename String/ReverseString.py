from collections import defaultdict
def stringCompression(s):
	#store = defaultdict(int)
	#for i in range(len(s)):
	#	store[s[i]] += 1
	#result = []
	#for key, val in store.items():
	#	if val != 1:
	#		result.extend([key]+list(str(val)))
	#	else:
	#		result.append(key)
	#return result, len(result)
	count = 0
	anchor = 0
	for idx, val in enumerate(s):
		if s[idx] == s[idx+1]:
			count = count + 1
		else:
			anchor = idx+1
			
		
s = ["a","b","b","b","b","b","b","b","b","b","b","b","b",]
print(stringCompression(s))
			
		
			
			