def ugly(n):
	i,j,k = 1,1,1
	two = 2*i
	three = 3*j
	five = 5*k
	count = 0
	while count <= n:
		pick_list = [2*i,3*j,5*k]
		mini = min(pick_list)
		idx = pick_list.index(mini)
		result = mini
		#print(pick_list)
		print(mini, end="-")
		count = count + 1
		if idx == 0:
			i = i+1
			while (2*i in pick_list) or (i%2 !=0 and i%3 != 0 and i%5 != 0):
				i = i+1

		elif idx == 1:
			j = j+1
			while (3*j in pick_list) or (j%2 !=0 and j%3 != 0 and j%5 != 0):
				j = j+1
	
		elif idx == 2:
			k = k+1
			while (5*k in pick_list) or (k%2 !=0 and k%3 != 0 and k%5 != 0):
				k = k+1
	#return result
nums = []
print(ugly(25))			
				
		
			
	
	