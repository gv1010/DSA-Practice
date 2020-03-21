def countingBits(num):
	if num == 0:
		return 0
	n = num
	prime = 1
	result = [0]*(num+1)
	result[1] = 1
	while n//2 != 0:
		prime = prime*2
		result[prime] = 1
		n = n//2
	for i in range(2, num+1):
		if result[i] == 1:
			base = i
			continue
		print(base)
		result[i] = 1 + result[i-base]
	return result
	
num = 13
print(countingBits(num))
	
		