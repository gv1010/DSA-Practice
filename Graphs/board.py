import copy
def dfs(board, i, j):
	if i < 1 or j < 1 or i > len(board)-1 or j > len(board[0])-1 or board != "X":
		return
	board[i][j] = "X"
	dfs(board, i+1, j)
	dfs(board, i-1, j)
	dfs(board, i, j+1)
	dfs(board, i, j-1)
	
grid = [['X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'X'],
		['X', 'X', 'O', 'X'],
		['X', 'O', 'X', 'X']]
board = copy.deepcopy(grid) 
for i in range(1,len(board)-1):
	for j in range(1,len(board[0])-1):
		if board[i][j] == 'O':
			dfs(board, i, j)
print(board)