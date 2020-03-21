import math
# Write your code here
def bestIndex(array):
	length = len(array)
	cells = int(-1 + math.sqrt(8*length + 1))/2
	print(cells)
	for i in range(int(cells)):
		print(array[i:i+1])


array = [1,3,4,5,5,6]
bestIndex(array)