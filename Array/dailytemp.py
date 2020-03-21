def dailytemp(T):
	#from collections import defaultdict
	#res = [0]*len(T)
	#for i in range(len(T)):
	#	for j in range(i+1, len(T)):
	#		if T[j] > T[i] :
	#			res[i] = j-i
	#			break
	#return res
	#msf = float('-inf')
	#res = [0]*len(T)
	#for i, temp in enumerate(T[::-1]):
	#	if temp >= msf:
	#		msf = temp
	#		res[len(T)-1-i] = 0
	#	else:
	#		count = 0
	#		length = T[len(T)-i:]
	#		while length:
	#			count = count + 1
	#			if val > temp:
	#				res[len(T)-1-i] = count
	#				break
	#			length = length - 1
	#print(res)
	store = [float('inf')]*105
	res = [0]*len(T)
	for i in range(len(T)-1,-1,-1):
		nxtWarm = min(store[T[i]+1:])
		if nxtWarm < float('inf'):
			res[i] = nxtWarm-i
		store[T[i]] = i
	return res
		
		
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailytemp(T))			
				
	
