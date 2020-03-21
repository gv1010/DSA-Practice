import math
import time

def fibiter(n):
	if n == 1:
		return 0
	f1=1
	f2=1
	for i in range(2,int(n)-1):
		f1,f2=f2,f1+f2
	return f2
	

def fibiter1(k):

	if (k%4 == 2):
		return 2
	if (k%4 == 3):
		return 3
	if ( k%4 == 0): 
		return 0
	if (k%4 == 1):
		return 9
	
def fun(n):
	if n < 4:
		if n == 3 or n == 2:
			return 1
		if n == 1:
			return 0
	else:
		return fibiter1( math.floor(math.log(n,2)))

a = int(input())
if a > 0:
	for i in range(0, a): 
		b = int(input())
		if b > 0:
			print(fun(b))
		else:
			print('Input should be +ve')
else:
	print('Input should be positive number')

	