import math
import time

def surya(n):
	a = 0
	b = 1
	for i in range(0, int(n)):
		a = b
		b = a+b
	return a

#def fun(n):
#	k = math.floor(math.log(n,2))
#	return fib((math.pow(2,k)) % 10)


start = (time.time())

print(surya(4))

print(time.time()- start)
#a = int(input())
#lis = []
#for i in a:
	
	