#s1 < s2
from collections import defaultdict
def checkInclusion(s1, s2):
	def check(s1map, s2map):
		for i in s2map:
			if s1map[i] != s2map[i]:
				return False
		return True
	if len(s1) > len(s2):
		return False
	s1map = defaultdict(int)
	s2map = defaultdict(int)
	len1 = len(s1)
	for i in s1:
		s1map[i] = s1map[i]+1
	for j in range(len(s1)):
		s2map[s2[j]] = s2map[s2[j]]+1
	if check(s1map, s2map):
			return True
	i = 0
	j = len1
	while j < len(s2):
		s2map[s2[j]] = s2map[s2[j]] + 1
		s2map[s2[i]] = s2map[s2[i]] - 1
		i=i+1
		j=j+1
		#print(s1map, s2map)
		if check(s1map, s2map):
			return True
		#s2map = defaultdict(int)
		#for k in range(i,j+1):
		#	s2map[s2[k]] = s2map[s2[k]]+1
		#if check(s1map, s2map):
		#	return True
		#i = i+1
		#j = j+1
	return False
	
s1 = "a" 
s2 = "ab"

print(checkInclusion(s1, s2))