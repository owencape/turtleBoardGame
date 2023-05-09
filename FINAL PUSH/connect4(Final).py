import turtle
import random

#creators: Owen Cape & Ty Tichenor
#finished 5/8/2023

# source for some of the base code
# https://www.youtube.com/watch?v=UYgyRArKDEs
# a little bit of stack overflow was used also

#vars
gameOver=False
message = ''
pieceList = []
x_list = [-300, -200, -100, -0, 100, 200, 300]
y_list = [200, 100, 0, -100, -200, -300]


board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    ]


#wn setup
wn = turtle.Screen()
wn.title('Connect 4')
wn.setup(950, 800)
wn.bgcolor('deepskyblue1')
wn.tracer(0)
wn.listen()


#add shapes
wn.addshape("pvc.gif")
wn.addshape("pvp.gif")
wn.addshape("connect4.gif")
wn.addshape("redChip.gif")
wn.addshape("blueChip.gif")
wn.addshape("stack.gif")
wn.addshape("youTube.gif")


#turtle setup
menu = turtle.Turtle()
keys = turtle.Turtle()
pvc = turtle.Turtle("pvc.gif")
pvp = turtle.Turtle("pvp.gif")
connect4 = turtle.Turtle("connect4.gif")
redChip = turtle.Turtle("redChip.gif")
blueChip = turtle.Turtle("blueChip.gif")
stack = turtle.Turtle("stack.gif")
youTube = turtle.Turtle("youTube.gif")

#starting needs
applied = False
menu.speed(0)
menu.penup()
pvc.hideturtle()
pvc.penup()
pvp.hideturtle()
pvp.penup()
connect4.hideturtle()
redChip.penup()
redChip.hideturtle()
blueChip.penup()
blueChip.hideturtle()
youTube.penup()
youTube.hideturtle()
stack.penup()
stack.hideturtle()
keys.penup()
keys.hideturtle()


def mainMenu():
    menu.clear()
    pvc.clear()
    pvp.clear()
    connect4.clear()
    redChip.clear()
    blueChip.clear()
    youTube.clear()
    stack.clear()
    keys.clear()
    menu.goto(-200,250)
    menu.write("CONNECT 4", font=("Arial",50,"bold"))
    menu.fd(-10)
    menu.left(90)
    menu.color("goldenrod1")
    menu.pensize(5)
    menu.pendown()
    menu.fd(80)
    menu.right(90)
    menu.fd(410)
    menu.right(90)
    menu.fd(80)
    menu.right(90)
    menu.fd(410)
    pvc.goto(0,100)
    pvc.stamp()
    keys.goto(0,0)
    keys.color("black")
    keys.write("Press C to Play!", font=("Arial",15,"bold"), align = "center")
    menu.penup()
    menu.right(180)
    menu.goto(-150,0)
    menu.pendown()
    menu.color("black")
    menu.fd(300)
    menu.penup()
    menu.hideturtle()
    pvp.goto(0,-100)
    pvp.stamp()
    keys.goto(0,-200)
    keys.color("black")
    keys.write("Press P to Play!", font=("Arial",15,"bold"), align = "center")
    connect4.penup()
    connect4.goto(0,-275)
    connect4.stamp()
    keys.goto(-250,-250)
    keys.color("black")
    keys.write("Press D to show Directions", font=("Arial",15,"bold"), align = "center")
    keys.goto(250,-250)
    keys.color("black")
    keys.write("Press V to show Credits", font=("Arial",15,"bold"), align = "center")
    redChip.goto(-290,150)
    redChip.stamp()
    redChip.goto(-290,75)
    redChip.stamp()
    redChip.goto(-290,0)
    redChip.stamp()
    redChip.goto(-290,-75)
    redChip.stamp()
    blueChip.goto(290,150)
    blueChip.stamp()
    blueChip.goto(290,75)
    blueChip.stamp()
    blueChip.goto(290,0)
    blueChip.stamp()
    blueChip.goto(290,-75)
    blueChip.stamp()
    
def credits():
    #clearing marks
    menu.clear()
    pvc.clear()
    pvp.clear()
    connect4.clear()
    redChip.clear()
    blueChip.clear()
    youTube.clear()
    stack.clear()
    keys.clear()
    menu.goto(-150,200)
    menu.color("goldenrod1")
    menu.write("CREDITS", font=("Arial",50,"bold"))
    menu.penup()
    menu.goto(-90,165)
    menu.write("Authors:", font=("Verdana",25,"bold"))
    menu.penup()
    menu.goto(-160,130)
    menu.write("Owen Cape & Ty Tichenor", font=("Times New Roman",20,"bold"))
    menu.penup()
    menu.goto(-125,0)
    menu.write("Sources:", font=("Arial",40,"bold"))
    menu.goto(0,-225)
    menu.color("black")
    menu.write("Press Q to go to MAIN MENU", font=("Verdana",25,"bold"), align = "center")
    #logos
    stack.penup()
    stack.goto(-175,-100)
    stack.stamp()
    stack.hideturtle()
    youTube.penup()
    youTube.goto(100,-100)
    youTube.stamp()
    youTube.hideturtle()
    
def directions():
    menu.clear()
    pvc.clear()
    pvp.clear()
    connect4.clear()
    redChip.clear()
    blueChip.clear()
    youTube.clear()
    stack.clear()
    keys.clear()
    menu.goto(-190,200)
    menu.color("goldenrod1")
    menu.write("DIRECTIONS", font=("Arial",50,"bold"))
    menu.penup()
    menu.goto(-50,150)
    menu.color("black")
    menu.write("PVC:", font=("Verdana",25,"bold"))
    menu.color("goldenrod1")
    menu.penup()
    menu.goto(0,90)
    menu.write("Use arrow keys to move piece...hit space to drop...\ncomputer will automatically play...first to four in a row wins!", font=("Times New Roman",20,"bold"), align = "center")
    menu.penup()
    menu.goto(-50,50)
    menu.color("black")
    menu.write("PVP:", font=("Verdana",25,"bold"))
    menu.color("goldenrod1")
    menu.penup()
    menu.goto(0,0)
    menu.write("Use arrow keys to move piece...hit space to drop\n...first to four in a row wins!", font=("Times New Roman",20,"bold"), align = "center")
    menu.penup()
    menu.goto(0,-225)
    menu.color("black")
    menu.write("Press Q to go to MAIN MENU", font=("Verdana",25,"bold"), align = "center")
    
def pvpStart():
    global message
    global gameOver
    #clears menu
    menu.clear()
    pvc.clear()
    pvp.clear()
    connect4.clear()
    redChip.clear()
    blueChip.clear()
    youTube.clear()
    stack.clear()
    keys.clear()
    #prints board
    for i in x_list:
        for j in y_list:
            tile = Tile()
            tile.goto(i,j)

            piece = Piece('black', 'still')
            piece.goto(i,j)
    #pvp control movement
    piece1 = Piece('red', 'move')
    piece1.goto(0, 300)

    wn.onkey(piece1.move_right, 'Right')
    wn.onkey(piece1.move_left, 'Left')
    wn.onkey(piece1.dropNormal, 'space')

    gameOver = False
    message = ''
    #checks if board full
    while not gameOver:
        if len(pieceList) >= 42:
            gameOver = True
        wn.update()

    print("GAME OVER")
    text = turtle.Turtle()
    text.up()
    text.hideturtle()
    #prints winning person text
    if message == 'Red Wins!!':
        text.color('red')
    else:
        text.color('lime')
    text.goto(0, 280)
    text.write(f'GAME OVER, {message}', align='center', font=('Courier', 36, 'bold'))

def pvcStart():
    global gameOver
    #clears menu
    menu.clear()
    pvc.clear()
    pvp.clear()
    connect4.clear()
    redChip.clear()
    blueChip.clear()
    youTube.clear()
    stack.clear()
    keys.clear()
    #displays board
    for i in x_list:
        for j in y_list:
            tile = Tile()
            tile.goto(i,j)

            piece = Piece('black', 'still')
            piece.goto(i,j)
    #player movement in PVC
    piece1 = Piece('red', 'move')
    piece1.goto(0, 300)
    wn.onkey(piece1.move_right, 'Right')
    wn.onkey(piece1.move_left, 'Left')
    wn.onkey(piece1.drop, 'space')
    #sees if board is full
    while not gameOver:
        
        if len(pieceList) >= 42:
            gameOver = True
        wn.update()

    print("GAME OVER")
    text = turtle.Turtle()
    text.up()
    text.hideturtle()
    if message == 'Red Wins!!':
        text.color('red')
    else:
        text.color('lime')
    text.goto(0, 280)
    text.write(f'GAME OVER, {message}', align='center', font=('Courier', 36, 'bold'))

def dropPiece(board, row, col, piece):
    board[row][col] = piece


def fourInRow(board,piece):
    #looked at wordsearch code to help me check horizontal
    for c in range(4): #limits that you can't get 4 in the last three columns
        for r in range(7):
            if board[r][c] == piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

    #Vertical 
    for c in range(7): 
        for r in range(4):  #Can't get 4 in row in the last 3 rows
            if board[r][c] == piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

    #Check positively sloped diagonals
    for c in range(4): #Can only get 4 in row in some positive diagonals
        for r in range(4):
            if board[r][c] == piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    #Check negatively sloped diagonals
    for c in range(7): 
        for r in range(3, 7): #Can only get 4 in row in some neg diagonals
            if board[r][c] == piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
            

class Tile(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.shapesize(5, 5)
        self.up()
        self.color('yellow')


class Piece(turtle.Turtle):
    def __init__(self, color, state):
        super().__init__(shape='circle')
        self.shapesize(4.5, 4.5)
        self.up()
        self.c = color
        self.color(self.c)
        self.state = state
        
    def move_right(self):
        if self.xcor()<300 and self.state == 'move':
            self.goto(self.xcor()+100, self.ycor())

    def move_left(self):
        if self.xcor()>-300 and self.state =='move':
            self.goto(self.xcor()-100, self.ycor())
    #modified just for PVP (no random drops)
    def dropNormal(self):
        global pieceList
        global gameOver
        global board
        global message
        
        # Create new piece to be dropped
        dropped_piece = turtle.Turtle()
        dropped_piece.shape('circle')
        dropped_piece.shapesize(4.5, 4.5)
        dropped_piece.color(self.c)
        dropped_piece.up()

        # Check drop position in y list
        for i in y_list[::-1]:
            #print(i)

            if (self.xcor(),i) not in pieceList:
                ypos = i
                break
            else:
               
                if (self.xcor(), 200) in pieceList:
                    ypos = 1000  # Hide off screen if column is full
                    print("cannot add to the column")
            
                
        dropped_piece.goto(self.xcor(), ypos)
        xcor = dropped_piece.xcor()
        ycor = dropped_piece.ycor()
        
        # Only add to the list if dropped within the grid
        if ycor != 1000:
            pieceList.append((xcor,ycor))
                        
        # Change color of the player piece
        if self.c == 'red':
            piece = 1 
            self.c = 'lime'
            self.color(self.c)
        else:
            self.c = 'red'
            self.color(self.c)
            piece = 2

        
        dropPiece(board, x_list.index(xcor), y_list.index(ycor), piece)
        

        # Check winning move
        if fourInRow(board,1):
            wn.update()
            gameOver = True
            message = 'Red Wins!!'
            return
        
        if fourInRow(board,2):
            wn.update()
            gameOver = True
            message = 'Green Wins!!'
            return
    #modified drop function for PVC
    def drop(self):
        global pieceList
        global gameOver
        global board
        global message
        global piece
        
        #Create new piece to be dropped
        droppedPiece = turtle.Turtle()
        droppedPiece.shape('circle')
        droppedPiece.shapesize(4.5, 4.5)
        droppedPiece.color(self.c)
        droppedPiece.up()
        
        #Check drop position in y list
        for i in y_list[::-1]:
            #print(i)

            if (self.xcor(),i) not in pieceList:
                ypos = i
                break
            else:
               
                if (self.xcor(), 200) in pieceList:
                    ypos = 1000  #Hide off screen if column is full
                    print("cannot add to the column")
                       
        droppedPiece.goto(self.xcor(), ypos)
        xcor = droppedPiece.xcor()
        ycor = droppedPiece.ycor()
        
        #Only add to the list if dropped within the board
        if ycor != 1000:
            pieceList.append((xcor,ycor))
                        
        #Change color of the player piece
        if self.c == 'red':
            piece = 1 
            self.c = 'lime'
            self.color(self.c)
        else:
            self.c = 'red'
            self.color(self.c)
            piece = 2 

        #Drop in grid using index positions and the piece (red = 1 and lime=2)
    
        dropPiece(board, x_list.index(xcor), y_list.index(ycor), piece)

        # Check winning move
        if fourInRow(board,1):
            wn.update()
            gameOver = True
            message = 'Red Wins!!'
            return
        if fourInRow(board,2):
            wn.update()
            gameOver = True
            message = 'Green Wins!!'
            return
         
        #computer's turn 
        droppedPiece2 = turtle.Turtle()
        droppedPiece2.shape('circle')
        droppedPiece2.shapesize(4.5, 4.5)
        droppedPiece2.color(self.c)
        droppedPiece2.up()
        
        #Change color of the player piece
        if self.c == 'red':
            piece = 1
            self.c = 'lime'
            self.color(self.c)
        else:
            self.c = 'red'
            self.color(self.c)
            piece = 2
        
        #selects random x index
        xPoint = random.randrange(6)   
        x = x_list[xPoint]

        #Check drop position in y list
        for i in y_list[::-1]:
            #print(i)
            #controls random x drop points
            if (x,i) not in pieceList:
                ypos = i
                break
            else:
               
                
                if (x, 200) in pieceList:
                    ypos = 1000  #Hide off screen if column is full
                    print("cannot add to the column")
        
                      
        droppedPiece2.goto(x, ypos)
        xcor = droppedPiece2.xcor()
        ycor = droppedPiece2.ycor()
        
        if ycor != 1000:
            pieceList.append((xcor,ycor))
                        
            
        #Drop in grid using index positions and the piece (red = 1 and lime=2)
        dropPiece(board, xPoint, y_list.index(ycor), piece)

        # Check winning move
        if fourInRow(board,1):
            wn.update()
            gameOver = True
            message = 'Red Wins!!'
            return
        if fourInRow(board,2):
            wn.update()
            gameOver = True
            message = 'Green Wins!!'
            return

                   
wn.onkeypress(pvpStart,"p")
wn.onkeypress(pvcStart,"c")
wn.onkeypress(credits,"v")
wn.onkeypress(directions,"d")
wn.onkeypress(mainMenu,"q")

            
mainMenu()


wn.mainloop()
     