def short(p, s):
	
	min_size = len(p)
	start_i = 0
	end_j = 0
	for i in range(len(p)):
		q = s
		if p[i] in q:
			j = i+1
			start = j
			while j<len(p) and len(q)!=0:
				if p[j] in q:
					q.replace(p[j], '')
				j = j+1
			if j != 0 and j-start < min_size and len(q) == 0:
				min_size = j-start
				print(p[start-1:j+1])
		s = 'aei'
	return p[start:start+min_size]
p = "figehaeci"
s = "aei"
print(short(p,s))
	

				