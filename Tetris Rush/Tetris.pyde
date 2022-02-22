import random, copy

#number of rows and column
NUM_ROWS = 20
NUM_COLS = 10
#using number of rows and columns to calculate window size
RES_WIDTH = NUM_COLS * 20
RES_HEIGHT = NUM_ROWS * 20



score = 0

mouse_clicked = False

class Block():
    def __init__(self, row, col, c = 0):
        #size of the block in pixels
        self.dimension = 20
        #row and col of the place where block should be created
        self.row = row
        self.col = col
        if c == 0:
            self.c = random.randint(1,7)
        else:
            self.c = c
        
    def display(self):
        #giving the attribute color a value based on randomly picked value between 1 and 7
        if self.c == 1:
            # Red: 255, 51, 52
            fill(255, 51, 52)
        elif self.c ==2:
            # Blue: 12, 150, 228
            fill (12,150,228)
        elif self.c == 3:
            # Green: 30, 183, 66
            fill(30,183,66)
        elif self.c == 4:
            #Yellow: 246, 187, 0
            fill (246,187,0)
        elif self.c ==5:
            # Purple: 76, 0, 153
            fill (76,0,153)
        elif self.c ==6:
            # White: 255, 255, 255
            fill (255,255,255)
        else:
            fill(0,0,0)
            # Black: 0, 0, 0
            
        rect(self.col * self.dimension, self.row * self.dimension, self.dimension, self.dimension)
        
    #FOR DEBUGGING PURPOSE
    def __str__(self):
        string = "row: " + str(self.row) + " col: " + str(self.col) + " colour: " + str(self.c)
        return string

class Game(list):
    def __init__(self):
        # self = []
        for row in range(NUM_ROWS):
            row_list = []
            for col in range(NUM_ROWS):
                row_list.append("")
            self.append(row_list)
        
        self.speed= 0
        self.AddBlock()
        
        #for handling key presses
        self.key_handler = {LEFT:False, RIGHT: False}
            
    def display(self):
        

    
        #Printing background 
        for i in range(NUM_COLS):
            noFill()
            stroke(180, 180, 180)
            rect(i * 20, 0, RES_WIDTH, RES_HEIGHT)
        
        for i in range(NUM_ROWS * 2):
            noFill()
            stroke(180, 180, 180)
            rect(0, i * 20, RES_WIDTH, RES_HEIGHT)
            
        #printing blocks
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):    
                if self[row][col] != "":
                    self[row][col].display()
        
        #printing score
        fill(12,150,255)
        textSize(15)
        string = "Score: " + str(score)
        text(string, RES_WIDTH - 80, 15)
                
    def AddBlock(self):
        #randomly picking column for new block, keeps looks for other column if this one is already filled
        valid = False
        self.row = 0
        while valid == False:
            self.col = random.randint(0, NUM_COLS -1)
            if self[self.row][self.col] == "":
                valid = True
                
        
        self[self.row][self.col] = Block(self.row, self.col)
        
    def MoveBlock(self):
        #moving the block one row down
        try:
            tempr = self.row
            tempcol = self.col
            tempc = self[self.row][self.col].c
    
            self[self.row + 1][self.col] = Block(tempr + 1, tempcol, tempc)
            self[self.row][self.col] = ""
            self.row +=1
            # print("moved down")
            
            #MOVING BLOCKS ACCORDING TO KEY PRESSES
                #first condition checks for key pressed, second condition makes sure block remains inside grid, third condition ensures no overlapping of blocks.
            if self.key_handler[LEFT] == True and self.col > 0 and self[self.row][self.col-1] == "" :
                self[self.row][self.col-1] = Block(self.row, tempcol -1, tempc)
                self[self.row][self.col] = ""
                self.col -=1
                # print("MOVED LEFT")
            elif self.key_handler[RIGHT] == True and self.col < NUM_COLS - 1 and self[self.row][self.col+1] == "" :
                self[self.row][self.col + 1] = Block(self.row, tempcol + 1, tempc)
                self[self.row][self.col] = ""
                self.col +=1
                # print("MOVED RIGHT")
            
            
            self.CheckStack()
        except:
            None
    
        
    def CheckStack(self):
        self.stack = False
        if self.row == NUM_ROWS - 1:
            #block is at the bottom
            return True
                
        elif self[self.row+1][self.col] != "":
            #row below already has a block
            return True
            
            
        else:
            #block should keep falling down
            return False
        
    def CheckLoss(self):
        count = 0
        for i in range(NUM_COLS):
            if self[0][i] !="" and self[1][i] !="":
                count +=1
        
        if count == NUM_COLS:
            return True
        else:
            return False
    
    def CheckMatch(self):
        global score
        count = 0
        try:
            for i in range(4):
                if self[self.row][self.col].c == self[self.row + i][self.col].c:
                    count += 1
        except:
            # print("index error")
            None
            
        if count == 4:
            # print("----------------------------")
            for i in range(4):
                self[self.row + i][self.col] = ""
            self.speed = 0
            score += 1
        
game = Game()

#Function that is called when game is running. Needed this so we can replay on a mouse click.
def game_phase():
    if game.CheckStack():
        game.CheckMatch()
        game.AddBlock()
        game.speed +=0.25
    else:
        game.MoveBlock()
        
def setup():
    size(RES_WIDTH, RES_HEIGHT)
    
    
def draw():

    #slow down the game by not displaying every frame
    if frameCount%(max(1, int(8 - game.speed)))==0 or frameCount==1:
        global mouse_clicked
        global score
        background(210)
        #this calls the display method of the game class
        game.display()
        if not game.CheckLoss():
            game_phase()
            
        else:
            fill(255,255,255)
            rect(0,0, RES_WIDTH, RES_HEIGHT)
            fill(0,0,0)
            textSize(20)
            string = "GAME OVER!"
            text(string, RES_WIDTH // 10, RES_HEIGHT // 3)
            string = "Your Score: " + str(score)
            textSize(15)
            text(string, RES_WIDTH // 10, RES_HEIGHT // 2)
            textSize(10)
            text("Click to play again", RES_WIDTH // 4, RES_HEIGHT // 1.5)

            
        if game.CheckLoss and mouse_clicked == True:
            for i in range(NUM_ROWS -1 , -1, -1):
                game.pop(i)
            score = 0
            game.__init__()
            game_phase()
            
            mouse_clicked = False
            
                
def keyPressed():
    if keyCode in game.key_handler:
        game.key_handler[keyCode] = True
        
def keyReleased():
    if keyCode in game.key_handler:
        game.key_handler[keyCode] = False  
    
def mouseClicked():
    global mouse_clicked
    if game.CheckLoss():
        mouse_clicked = True
    
        
        
