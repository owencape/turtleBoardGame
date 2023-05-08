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

#red piece will drop first
def dropPiece(board, row, col, piece):
    board[row][col] = piece


def fourInRow(board,piece):
    #looked at wordsearch code to help me check horizontal
    for c in range(4): #limits that you can't get 4 in the last three columns
        for r in range(7):
            if board[r][c] == piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True

    # Vertical 
    for c in range(7): 
        for r in range(4):  # Can't get 4 in row in the last 3 rows
            if board[r][c] == piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

    # Check positively sloped diagonals
    for c in range(4): # Can only get 4 in row in some positive diagonals
        for r in range(4):
            if board[r][c] == piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True

    # Check negatively sloped diagonals
    for c in range(7): 
        for r in range(3, 7): # Can only get 4 in row in some neg diagonals
            if board[r][c] == piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True
            

wn = turtle.Screen()
wn.title('Connect 4')
wn.setup(950, 800)
wn.bgcolor('deepskyblue1')
wn.tracer(0)
wn.listen()
piece_list = []

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
        global piece_list
        global game_over
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

            if (self.xcor(),i) not in piece_list:
                ypos = i
                break
            else:
               
                #print('In the list')
                if (self.xcor(), 200) in piece_list:
                    ypos = 1000  # Hide off screen if column is full
                    print("cannot add to the column")
            
        # os.system('afplay drop.wav&')                
        dropped_piece.goto(self.xcor(), ypos)
        xcor = dropped_piece.xcor()
        ycor = dropped_piece.ycor()
        
        # Only add to the list if dropped within the grid
        if ycor != 1000:
            piece_list.append((xcor,ycor))
                        
        # Change color of the player piece
        if self.c == 'red':
            piece = 1 # for numpy board below
            self.c = 'lime'
            self.color(self.c)
        else:
            self.c = 'red'
            self.color(self.c)
            piece = 2 # for numpy board below

        # Drop in numpy grid using index positions and the piece (red = 1 and yellow=2)
        # print(x_list.index(xcor))
        # print(y_list.index(ycor))
        dropPiece(board, x_list.index(xcor), y_list.index(ycor), piece)
        #for i in board:
            #print(i)
        #print()

        # Check winning move
        if fourInRow(board,1):
            wn.update()
            game_over = True
            message = 'Red Wins!!'
        if fourInRow(board,2):
            wn.update()
            game_over = True
            message = 'Green Wins!!'


x_list = [-300, -200, -100, -0, 100, 200, 300]
y_list = [200, 100, 0, -100, -200, -300]

# Place blue 100x100 background tiles and fill with black circles/pieces
for i in x_list:
    for j in y_list:
        tile = Tile()
        tile.goto(i,j)

        piece = Piece('black', 'still')
        piece.goto(i,j)

# Create player piece - red that will move with left or right keys
piece1 = Piece('red', 'move')
piece1.goto(0, 300)

wn.onkey(piece1.move_right, 'Right')
wn.onkey(piece1.move_left, 'Left')
wn.onkey(piece1.drop, 'space')

game_over = False
message = ''


while not game_over:
    if len(piece_list) >= 42:
        game_over = True
    wn.update()

print("GAME OVER")
pen = turtle.Turtle()
pen.up()
pen.hideturtle()
if message == 'Red Wins!!':
    pen.color('red')
else:
    pen.color('lime')
pen.goto(0, 280)
pen.write(f'GAME OVER, {message}', align='center', font=('Courier', 36, 'bold'))

wn.mainloop()