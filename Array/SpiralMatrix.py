def spiralMatrix(num ):
	v = 0
	top = 0
	left = 0
	right = num-1
	down = num-1
	nums = [[0 for i in range(num)] for j in range(num) ]
	count = 0
	while top<=down and left <= right:
		if v == 0:
			for i in range(left, right+1):
				count = count+1
				nums[top][i] = count
			top = top+1
			v = 1
		elif v == 1:
			for i in range(top, down+1):
				count = count+1
				nums[i][right] = count
			right = right-1
			v = 2
			
		elif v == 2:
			for i in range(right, left-1,-1):
				count = count+1
				nums[down][i] = count
			down = down-1
			v = 3
		elif v == 3:
			for i in range(down, top-1,-1):
				count = count+1
				nums[i][left] = count
			left = left+1
			v = 0
	return nums
def spiralOrder(matrix):
	v = 0
	top = 0
	left = 0
	right = len(matrix[0])-1
	down = len(matrix)-1
	nums = []
	if down == 0:
		return matrix
	if right == 0:
		return [mat[0] for mat in matrix]
	#for _ in range(len(matrix[0])*len(matrix)):
	while left <= right and top <= down:
		if v == 0:
			for i in range(left, right+1):
				nums.append(matrix[top][i])
			top = top+1
			v = 1
		elif v == 1:
			for i in range(top, down+1):
				nums.append(matrix[i][right])
			right = right-1
			v = 2
		elif v == 2:
			for i in range(right, left-1,-1):
				nums.append(matrix[down][i])
			down = down-1
			v = 3
		elif v == 3:
			for i in range(down, top-1,-1):
				nums.append(matrix[i][left])
			left = left+1
			v = 0
	return nums
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
#matrix = [
#  [1, 2, 3, 4],
#  [5, 6, 7, 8],
#  [9,10,11,12]
#]
#print(matrix)
print(spiralMatrix(4))
#print([1,2,3,4,8,12,11,10,9,5,6,7])	
		