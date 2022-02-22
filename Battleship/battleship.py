import random
import os
#Constants
DIMENSION = 10
SHIP_SIZE = 4

#initializing board
board = []

#variables to count number of guesses and number of hits
guesses = 0 
hits = 0 

#creating the board
for r in range(DIMENSION):
		row_list= []
		for c in range(DIMENSION):
			row_list.append(" ")

		board.append(row_list)

#RANDOMLY PLACING SHIP
#generating random initial location of ship 
valid = False
while valid == False:
	initial_location_row = random.randint(0,DIMENSION - 1)
	initial_location_column = chr(random.randint(65, (64 + DIMENSION)))
	asciicode = ord(initial_location_column)
	#generating random orientation of ship
	ship_row = [] 
	ship_orientation = random.randint(0,1)
	orientation = ["v", "h"]
	if orientation[ship_orientation] == "v":
		ship_column = [initial_location_column]
		if initial_location_row <DIMENSION - SHIP_SIZE + 1:
			#ship can fits facing down.
			show_row = [initial_location_row]
			for i in range(SHIP_SIZE):
				ship_row.append(initial_location_row + i)
			valid = True

	else:
		ship_row = [initial_location_row]
		if initial_location_column < chr(64 + DIMENSION - SHIP_SIZE): 
			#ship can fit going right
			ship_column = [initial_location_column]
			for z in range(SHIP_SIZE):
				ship_column.append(chr(asciicode+z))
			valid = True
			

#DETECTING END OF GAME. Keep running game until hits are 4 and the grid is printed.
while hits <SHIP_SIZE + 1:

	#Printing name of game
	os.system("clear")
	print("B", "A", "T", "T","L","E","S","H","I","P", sep = "     ")
	print("\n" * 2)
	#printing current score
	print("             guesses", guesses , "        hits:", hits)
	print("\n")

	#printing the board.
	for cols in range(65, 65 + DIMENSION):
		print('   ' + chr(cols), end="")
	print("\n +" + "---+" * DIMENSION)

	for row in range(DIMENSION):
		print(str(row) + "|", end = "  ")
		for col in range(DIMENSION):
			print(board[row][col] + "|", end = "  ")
		print("\n +" + "---+" * DIMENSION)

	#asking user for input and checking it. Keeps asking user until correct input is given or until end of game.
	while hits<SHIP_SIZE:
		coordinate = input("Enter a coordinate. Cooridnate must be a CAPITAL letter between A and J followed by a number between 0 and 9: ")
		coordinate_list = list(coordinate)

		#CHECKING FOR INVALID INPUT
		#checking if two items are input
		if len(coordinate_list) ==2:
			#checking if first item is alphabet fitting inside column.
			if coordinate_list[0].isalpha() and chr(65)<=coordinate_list[0]<=chr(64 + DIMENSION):
				#checking if second item is a number fitting inside rows.
				if coordinate_list[1].isdigit() and -1<int(coordinate_list[1])<DIMENSION:
					alphabet = coordinate_list[0]
					number = int(coordinate_list[1])
					
					#checking if coordinate has already been guessed
					if board[number][ord(alphabet) - 65] == " ":
						guesses += 1
						break
						#end loop because input is correct

		#Printing error values for each type of possible error.
					else:
						print("You have already guessed this coordinate. Try again.\n")
				else:
					print("A letter must be followed by a number between 0 and " + str(DIMENSION - 1) +". Try again.\n")
			else:
				print("Input must be a CAPITAL letter between A and " + chr(64+DIMENSION) + " followed by a number. Try again.\n")
		else:
			print("Incorrect input. Your coordinate should consist of two things. Try again.\n")


	#UPDATING BOARD CELLS. 
	if alphabet in ship_column and number in ship_row:
		hits = hits + 1
		#writing X if hit
		board[number][ord(alphabet) - 65] = "X"	
	else:
		#writing # if miss
		board[number][ord(alphabet) - 65] = "#"

print("\n" * 2)
#printing the final score to user.
print("Game over. You guessed :", guesses, "times.")	