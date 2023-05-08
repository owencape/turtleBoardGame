import turtle
import random
import winsound


board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    ]



# def checkFullBoard(board):
#         global goodSpot
#         for c in range(7):
#             for r in range(7):
#                 if board[r][c] == piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece and board[r+4][c]==piece and board[r+5][c]==piece and board[r+6][c]==piece:
#                     print("spot taken")
#         else:
#             goodSpot = True

#red piece will drop first
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
            

wn = turtle.Screen()
wn.title('Connect 4')
wn.setup(950, 800)
wn.bgcolor('deepskyblue1')
wn.tracer(0)
wn.listen()
pieceList = []

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
            
        print(ypos)             
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
        #for i in board:
            #print(i)
        #print()

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
        
        #Check drop position in y list
        xPoint = random.randrange(6)   
        x = x_list[xPoint]
        print(x)
        for i in y_list[::-1]:
            #print(i)

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
        #for i in board:
            #print(i)
        #print()

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

        
        
        
        
        
        
         
        # print(f"computer {computer}")
        # xPoint = random.randrange(6)
        # print(xPoint)
        # yPoint = random.randrange(6)
        # print(yPoint)
        # dropPiece(board, xPoint, yPoint, piece)
        
        #actually drop the piece
        
        #swap color
        
        #check for winner
            
        


x_list = [-300, -200, -100, -0, 100, 200, 300]
y_list = [200, 100, 0, -100, -200, -300]

#Place blue 100x100 background tiles and fill with black circles/pieces
for i in x_list:
    for j in y_list:
        tile = Tile()
        tile.goto(i,j)

        piece = Piece('black', 'still')
        piece.goto(i,j)

# Create player piece - red that will move with left or right keys
# piece1 = Piece('red', 'move')
# piece1.goto(0, 300)

# wn.onkey(piece1.move_right, 'Right')
# wn.onkey(piece1.move_left, 'Left')
# wn.onkey(piece1.drop, 'space')

gameOver = False
message = ''




     #if the symbol is x
     # then run the code already built
     #else
     # run the computer's code

     #loop until a good spot is chosen

        
            
     
piece1 = Piece('red', 'move')
piece1.goto(0, 300)
wn.onkey(piece1.move_right, 'Right')
wn.onkey(piece1.move_left, 'Left')
wn.onkey(piece1.drop, 'space')
#if we can NOT choose the spot
# checkFullBoard(board)

     #check for a winner or CAT
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

wn.mainloop()
     



