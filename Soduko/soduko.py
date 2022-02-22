import os, time

board = [
			[1," "," "," "," ",7," ",9," "],
			[" ",3," "," ",2," "," "," ",8],
			[" "," ",9,6," "," ",5," "," "],
			[" "," ",5,3," "," ",9," "," "],
			[" ",1," "," ",8," "," "," ",2],
			[6," "," "," "," ",4," "," "," "],
			[3," "," "," "," "," "," ",1," "],
			[" ",4," "," "," "," "," "," ",7],
			[" "," ",7," "," "," ",3," "," "]
		]

def print_board():
	os.system('clear')
	print ('-'*25, sep='')
	for row in range(len(board)):
		print ('|', end=' ')
		for col in range(len(board[0])):
			print (board[row][col], end=' ')
			if (col+1)%3 == 0:
				print ('|', end=' ')
		if (row+1)%3 == 0:
			print ('\n','-'*25, sep='')
		else:
			print()
	# time.sleep(0.5)

def valid_play(num,r,c):
    # horizontal
    if num in board[r]:
        return False

    # vertical
    for i in range(9):
        if board[i][c] == num:
            return False

    # sector
    for row in range(3*int(r/3), 3*int(r/3) + 3):
        for col in range(3*int(c/3), 3*int(c/3) + 3):
            if board[row][col] == num:
                return False

    return True

def get_next(r, c):
    if c < 8:
        return r, c+1
    return r+1, 0

def solver(r, c):

	# 1. Define exit condition, e.g. when r becomes larger than the board dimensions
	if r == len(board):
			#reached end of board
		return True

	# 2. Skip pre-filled cells. Use get_next() function to get next cell
	while board[r][c] != " ":
		r,c = get_next(r,c)
	# 3. Use brute force method (for loop) to fill the the current cells with a number (1-9)
	# 4. Verify if it is a valid play
	# 	a) if yes, move on to next cell and call solver() recursively
	# 	b) if not, try next number
	for num in range(1,10):
		if valid_play(num, r, c):
			board[r][c] = num
			print_board()
			nr, nc = get_next(r,c)
			if solver(nr, nc):
				return True


    # 5. return False if none of the above worked and reset cell
	board[r][c] = " "
	print_board()
	return False


solver(0,0)
print_board()
