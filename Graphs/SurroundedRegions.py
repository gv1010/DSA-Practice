def surround(board):
	stack = []
	for j in range(len(board[0])):
		if board[0][j] == "O" and board[1][j] == "O":
			stack.append((0,j))
		if board[len(board)-1][j] == "O"  and board[len(board)-2] == "O":
			stack.append((len(board)-1,j))
	for i in range(1, len(board)-1):
		if board[i][0] == "O"  and board[i][1] == "O":
			stack.append((i,0))
		if board[i][len(board[0])-1] == "O" and board[i][len(board[0])-2] == "O":
			stack.append((i, len(board[0])-1))
	def dfs(board, i, j, c):
		if i < 0 or j < 0 or i > len(board) or j > len(board[0]) or board[i][j] != "O":
			return 
		board[i][j] = c
		dfs(board, i+1, j, c)
		dfs(board, i-1, j, c)
		dfs(board, i, j+1, c)
		dfs(board, i, j-1, c)
		
	while stack != []:
		i, j = stack.pop()
		dfs(board, i, j, "*")
	
	for i in range(1, len(board)-1):
		for j in range(1, len(board[0])-1):
			if board[i][j] == "O":
				dfs(board, i, j, "X")
	return board
	
board = [['X', 'X', 'X', 'X'],
		['X', 'O', 'O', 'X'],
		['X', 'X', 'O', 'X'],
		['X', 'O', 'X', 'X']]
print(surround(board))
			
			