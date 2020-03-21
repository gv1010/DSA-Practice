def matrixRot(arr):
	for i in range(len(arr[0])):
		for j in range(i, len(arr[0])):
			arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
	for i in range(len(arr[0])):
		arr[i] = arr[i][::-1]
	print(arr)
	
arr = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(arr)
print(matrixRot(arr))