from collections import defaultdict
def allpalindromes(s):
	count = 0
	for i in range(len(s)):
		for j in range(i,len(s)):
			if s[i:j+1] == s[i:j+1][::-1]:
				count += 1
	return count
def longestPlaindrome(s):
	def expandatcenter(left, right):
		while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
			left = left-1
			right = right+1
		return right-left-1
	start = 0
	end = 0
	for i in range(len(s)):
		len1 = expandatcenter(i,i)
		len2 = expandatcenter(i,i+1)
		max_len = max(len1, len2)
		print(max_len)
		if max_len > end - start:
			start = i - (max_len-1)//2
			end = i + max_len//2
	#print(start, end)
	return s[start:end+1]
def validpalindrome(s):
	new = ""
	for alph in s:
		alph = alph.lower()
		if alph.isalnum():
			new = new + alph
	if new == new[::-1]:
		return True
	return False
def validPalindromeII(s):
	if s == s[::-1]:
		return True
	i = 0
	j = len(s)-1
	while i<j:
		if s[i] == s[j]:
			i = i+1
			j = j-1
		else:
			return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
	return True
			
	
		
	#count = 0
	#store = defaultdict(int)
	#for alph in s:
	#	alph = alph.lower()
	#	if alph.isalnum():
	#		store[alph] += 1
	#for key, val in store.items():
	#	if val%2 != 0:
	#		count += 1
	#print(store)
	#if count <= 2:
	#	return True
	#return False
	#if count == 0 or count == 1:
	#	return True
	#return False

s = "A man a plan a canal : Panama"
s = "racacar"
#s = "abca"
#s = "babbad"
s = "aaa"
print(allpalindromes(s))	