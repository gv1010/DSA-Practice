def wordBreak(s, wordDict):
	store = dict()
	for i in wordDict:
		store[i] = 1
	nums= [0]
	for i in range(1,len(s)+1):
		for j in nums[::-1]:
			#print(j)
			if s[j:i] in wordDict:
				nums.append(i)
				break
		print(nums)
		if nums[-1] == len(s):
			return True
	return False
				
	#for i in range(1,len(s)+1):
	#	if s[j:i] in wordDict and store[s[j:i]] == 1:
	#		new = new + s[j:i]
	#		store[s[j:i]] = 0
	#		j = i

			
s = "leetcode"
wordDict = ["leet", "code"]
s = "applepenapple"
wordDict = ["apple", "pen"]
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
#s = "aaaaaaa"
#wordDict = ["aaaa","aaa"]
print(wordBreak(s, wordDict))
		
	