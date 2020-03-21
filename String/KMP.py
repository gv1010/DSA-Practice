class KMP:
	#def __init__(self):
		
	def patternFunc(self, p):
		i = 0
		j = 1
		arr = [0]*(len(p))
		while j < len(p):
			if p[i] == p[j]:
				i = i+1
				arr[j] = i
				j = j+1
			else:
				if i != 0:
					i = arr[i-1]
				else:
					arr[j]=0
					j = j+1
		return arr
		
		#while j != len(p):	
		#	while j < len(p) and p[i] == p[j]:
		#		arr[j] = i+1
		#		i = i+1
		#		j = j+1
		#		while i != 0 and j < len(p) and p[i] != p[j]:
		#			i = arr[i-1]
		#			if p[i] == p[j]:
		#				arr[j] = i+1
		#				i = i+1
		#				j = j+1
		#				break
		#			
		#	if j < len(p) and p[i] != p[j]:
		#		print(1)
		#		arr[j] = 0
		#		j = j+1
		#return arr
		
k = KMP()
p = "aabaabaaa"
print(k.patternFunc(p))