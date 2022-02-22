import random, os, time


#randomly choosing one of the 12 files

file_number = random.randint(1,12) 
	#opening randomly chosen file
file_name = "board_"+str(file_number)+".csv"

board_file = open(file_name,"r")

	#Reading the first line to find dimensions and the words 
first_line = board_file.readline()
first_line = first_line.strip().split(",")
DIMENSIONS = int(first_line[0:1].pop())
words = first_line[2::]
	#total number of words to keep track of whether all have been guessed or not
TOTAL_WORD = len(words)

#initializing the board and populating it with board from csv file

board = []
for line in board_file:
	line = line.strip().split(",")
	line = line[0:DIMENSIONS]
	board.append(line)


#closing file because all needed data has been read
board_file.close()

os.system("clear")
valid = False
while valid == False:
	NUM_PLAYERS = input("Enter number of players: ")
	try:
		NUM_PLAYERS = int(NUM_PLAYERS)
		if NUM_PLAYERS > 0:
			valid = True
		else:
			print("Number must be greater than zero.")
	except:
		print("Must be a number. Try Again. \n")

player_turn = random.randint(1,NUM_PLAYERS)	


#make dictionary for each player as key and their guessed words list as the value
guess_dict ={}

for i in range(1, NUM_PLAYERS+1):
	guess_dict[i] = []

#Makes list to keep track of scores. Each player has 0 score at the start.
guessed_words = []
score = [""]
for i in range(NUM_PLAYERS+1):
	score.append(0)



#printing the board
def print_board():
	print("\n +" + "---+" * DIMENSIONS)

	for row in range(DIMENSIONS):
		print(" |", end = " ")
		for col in range(DIMENSIONS):
			print(board[row][col] + " |", end = " ")
		print("\n +" + "---+" * DIMENSIONS)

	if initial == False:
		print("\n")
		print("Score:")
		for i in range(1, NUM_PLAYERS+1):
			print("Player " + str(i) + ":", score[i], guess_dict[i])

	print()



#asking for input
def input_guess(player_turn):
	lower = True
	print_board()
	print("Player", player_turn, ", enter a (lower case) word: ", end = "")
	guess = input()
	if guess.isalpha():
		if len(guess)>=3:
			if guess.islower():

				if guess not in guessed_words:

					return guess

				else:
					print("Word has already been guessed. Player,", player_turn, "has lost their turn.")
			else:
				print("Guess must be lower case. Player,", player_turn, "has lost their turn.")
		else:
			print("Guess must be at least 3 letters. Player", player_turn, "has lost their turn.")
	else:
		print("Invalid input. Guess must be a word with letters between a and z only. Player", player_turn, "has lost their turn.")

def alternate_turn():
	global player_turn
	player_turn +=1
	if player_turn > NUM_PLAYERS:
		player_turn = 1


def check_match(row,col,guess):
	#HORIZONTAL CHECK
	if col < DIMENSIONS-1 and board[row][col+1] == guess[1]:
		#it goes right
		try:
			check = board[row][col:col+len(guess):]
			check = "".join(check)
			check = check.lower()
			if check == guess:
				#capitalizing the word matched
				for i in range(0,len(guess)):
					letter = board[row][col+i]
					letter = letter.upper()
					board[row][col+i] = letter
				return True
		except:
			None

	if col > 0 and board[row][col-1].lower() == guess[1]:
		#it goes left
		try:
			check = board[row][col:(col-DIMENSIONS-len(guess)): -1] 
			check = "".join(check)
			check = check.lower()
			if check == guess:
				for i in range(len(guess)-1,-1,-1):
					letter = board[row][col-i]
					letter = letter.upper()
					board[row][col-i] = letter
				return True
		except:
			None


	#VERTICAL CHECK

	if row != DIMENSIONS-1 and board[row+1][col].lower() == guess[1] and len(guess) + row <=DIMENSIONS:
		#it goes down
		count = 0
		z=0
		for i in range(row, row + len(guess)):
			if guess[z] == board[i][col].lower():
				count +=1
				z+=1

		if count == len(guess):
			#capitalizing the word matched
			for i in range(0,len(guess)):
				letter = board[row+i][col]
				letter = letter.upper()
				board[row+i][col] = letter
			return True		

	if row != 0 and board[row-1][col].lower() == guess[1] and row - len(guess) >= -1:
		#it goes up
		count = 0
		z=0
		for i in range(row, row -len(guess),-1):
			if guess[z] == board[i][col].lower():
				count +=1
				z+=1

		if count == len(guess):
			#capitalizing the word matched
			for i in range(0,len(guess)):
				letter = board[row-i][col]
				letter = letter.upper()
				board[row-i][col] = letter
			return True		


	#DIAGONAL CHECK

	
	if row < DIMENSIONS-1 and col <DIMENSIONS-1 and board[row+1][col+1].lower() == guess[1]:
		#it goes down right
		count = 0
		for i in range(0, len(guess)):
			try:
				if board[row+i][col+i].lower() == guess[i]:
					count +=1
			except:
				None
		if count == len(guess):
			#capitalizing the word matched
			for i in range(0,len(guess)):
				letter = board[row+i][col+i]
				letter = letter.upper()
				board[row+i][col+i] = letter
			return True

	if row < DIMENSIONS-1 and col>0 and board[row+1][col-1].lower() == guess[1]:
		#it goes down left
		count = 0
		try:
			for i in range(0, len(guess)):
				if board[row+i][col-i].lower() == guess[i]:
					count +=1	
		except:
			0	
		if count == len(guess):
			#capitalizing the word matched
			for i in range(0,len(guess)):
				letter = board[row+i][col-i]
				letter = letter.upper()
				board[row+i][col-i] = letter
			return True
		
	if row>0 and col<DIMENSIONS-1 and board[row-1][col+1].lower() == guess[1]:
		#it goes up right
		count = 0
		try:
			for i in range(0, len(guess)):
				if board[row-i][col+i].lower() == guess[i]:
					count +=1
		except:
			None		
		if count == len(guess):
			#capitalizing the word matched
			for i in range(0,len(guess)):
				letter = board[row-i][col+i]
				letter = letter.upper()
				board[row-i][col+i] = letter
			return True

	if row > 0 and col >0 and board[row-1][col-1].lower() == guess[1]:
		#it goes up left
		count=0
		try:
			for i in range(0, len(guess)):
				if board[row-i][col-i].lower() == guess[i]:
					count +=1
		except:
			None	

		if count == len(guess):
			#capitalizing the word matched
			for i in range(0,len(guess)):
				letter = board[row-i][col-i]
				letter = letter.upper()
				board[row-i][col-i] = letter
			return True

	#returns false if no match
	return False


#GAME RUNNING
total_guessed =0 
initial = True
while total_guessed < TOTAL_WORD:
	os.system("clear")
	guess = input_guess(player_turn)
	initial = False
	if guess !=None and guess in words:
		#finding location of letter in board, checking if that leads to a match
		for row in range(DIMENSIONS):
			for col in range(DIMENSIONS):
				if board[row][col].lower() == guess[0]:
					match = check_match(row,col,guess)
					if match == True:
						#checking if word is already in guessed list, this prevents double matches
						if not(guess in guessed_words):
							guessed_words.append(guess)
							score[player_turn] +=1
							player_listguessed = guess_dict[player_turn]
							player_listguessed.append(guess)
							guess_dict[player_turn]
							total_guessed +=1

	alternate_turn()
	time.sleep(1)


os.system("clear")
print_board()
print("Game Over!")

