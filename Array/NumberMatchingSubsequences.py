def subsequence(S, words):
	count = 0
	for w in words:
		i = 0
		j = 0
		while i < len(w) and j < len(S):
			if w[i] == S[j]:
				i+=1
				j+=1
				if i == len(w) and j <= len(S):
					count = count + 1
			else:
				j += 1
	return count
	
S = "abcde"
words = ["a", "bb", "acd", "ace"]
print(subsequence(S, words))
				
		
			