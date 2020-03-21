def lastdigit(a, b):
	if b <= 0:
		return 1
	if b%2 == 1:
		return a * (lastdigit(a, b-1)%10)
	else:
		res = lastdigit(a, b//2)%10
		return res*res
	
	
print(lastdigit(19,42375192507)%10)