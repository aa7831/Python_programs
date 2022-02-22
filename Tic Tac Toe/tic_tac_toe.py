import random, os

DIM = 3
NUM_PLAYERS = 2
CHECKERS = ['', 'X', 'O']
board = []

player_turn = random.randint(1,NUM_PLAYERS)

# print the board
def print_board():
	os.system('clear')
	for cols in range(DIM):
		print('   ' + str(cols), end='')

	print("\n +" + "---+" * DIM)

	for row in range(DIM):
		print(str(row) + '|', end=' ')
		for col in range(DIM):
			print(board[row][col] + ' | ', end='')
		print("\n +"+"---+"*DIM)


# check for a win condition
def check_win(r, c):
	# check horizontally and return True if its a win

	if board[r].count(CHECKERS[player_turn]) == DIM:
		return True

	# check vertically and return True if its a win

	count = 0

	for row in range(DIM):
		if board[row][c] == CHECKERS[player_turn]:
			count += 1

	if count == DIM:
		return True


	# check diagonally and return True if its a win

	count = 0
	count1 = 0
	for i in range(DIM):
		if board[i][i] == CHECKERS[player_turn]:
			count +=1

		if board[i][DIM - 1 -i] == CHECKERS[player_turn]:
			count1 +=1

	if count == DIM or count1 == DIM:
		return True


	# if none of the above return, return False
	return False


# create the board
for r in range(DIM):
	rowList = []
	for c in range(DIM):
		rowList.append(' ')
	board.append(rowList)


# game loop
win = False
while not win:
# 1. ask for input and validate it (error checking)
	valid = False
	while valid == False:
		print_board()
		coordinate = input("Player " + CHECKERS[player_turn] + ", please enter coordinate: ")
		if len(coordinate) == 2: 
			if coordinate.isdigit():
				if -1<int(coordinate[0]) < DIM and -1<int(coordinate[1])<DIM :
					r = int(coordinate[1])
					c = int(coordinate[0])
					valid = True
				else:
					print("coordinate must be number between 0 and ", DIM-1)
			else:
				print("coordinate must be number")
		else:
			print("coordinate must be two integers only")



# 2. place the checker and check for a win
	if board[r][c] == " ":
		board[r][c] = CHECKERS[player_turn]
		win = check_win(r,c)
		if win:
			print_board()
			print("Player", CHECKERS[player_turn], "won!")

# 3. alternate turn
	player_turn +=1
	if player_turn > NUM_PLAYERS:
		player_turn = 1

