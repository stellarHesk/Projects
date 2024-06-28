from tkinter import *
from tkinter import messagebox
#Initialize the root
root = Tk()
root.title("Tic Tac Toe")
#Initializae the canvas

#Constants
PLAYER_ONE = 1
PLAYER_TWO = 2
ROWS = COLUMNS = 3
EMPTY = 0
CANVAS_HEIGHT = ROWS * 200
CANVAS_WIDTH = COLUMNS * 200
#Initialize the board
board = [[EMPTY for x in range(COLUMNS)] for y in range(ROWS)]
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

#Player to start
current_player = PLAYER_ONE

def check_winner():
    '''
    Checks the board to see if there is a winner
    '''
    if (board[0][0] == PLAYER_ONE and board[0][1] == PLAYER_ONE and board[0][2] == PLAYER_ONE)\
    or (board[1][0] == PLAYER_ONE and board[1][1] == PLAYER_ONE and board[1][2] == PLAYER_ONE)\
    or (board[2][0] == PLAYER_ONE and board[2][1] == PLAYER_ONE and board[2][2] == PLAYER_ONE)\
    or (board[0][0] == PLAYER_ONE and board[1][1] == PLAYER_ONE and board[2][2] == PLAYER_ONE)\
    or (board[0][2] == PLAYER_ONE and board[1][1] == PLAYER_ONE and board[2][0] == PLAYER_ONE)\
    or (board[0][0] == PLAYER_ONE and board[1][0] == PLAYER_ONE and board[2][0] == PLAYER_ONE)\
    or (board[0][1] == PLAYER_ONE and board[1][1] == PLAYER_ONE and board[2][1] == PLAYER_ONE)\
    or (board[0][2] == PLAYER_ONE and board[1][2] == PLAYER_ONE and board[2][2] == PLAYER_ONE):
        return 1
    elif (board[0][0] == PLAYER_TWO and board[0][1] == PLAYER_TWO and board[0][2] == PLAYER_TWO)\
    or (board[1][0] == PLAYER_TWO and board[1][1] == PLAYER_TWO and board[1][2] == PLAYER_TWO)\
    or (board[2][0] == PLAYER_TWO and board[2][1] == PLAYER_TWO and board[2][2] == PLAYER_TWO)\
    or (board[0][0] == PLAYER_TWO and board[1][1] == PLAYER_TWO and board[2][2] == PLAYER_TWO)\
    or (board[0][2] == PLAYER_TWO and board[1][1] == PLAYER_TWO and board[2][0] == PLAYER_TWO)\
    or (board[0][0] == PLAYER_TWO and board[1][0] == PLAYER_TWO and board[2][0] == PLAYER_TWO)\
    or (board[0][1] == PLAYER_TWO and board[1][1] == PLAYER_TWO and board[2][1] == PLAYER_TWO)\
    or (board[0][2] == PLAYER_TWO and board[1][2] == PLAYER_TWO and board[2][2] == PLAYER_TWO):
        return 2
    #Check for draw
    draw = all(cell != EMPTY for row in board for cell in row)
    if draw:
        return 0
    return False


def draw_piece(row, column):
    """Draws each piece"""
    global current_player
    piece_drawn = False
    if board[row][column] == EMPTY:
        board[row][column] = current_player
        update_board()
        root.update_idletasks()
        piece_drawn = True
    if piece_drawn:
        #Check for a winner
        winner = check_winner()
        if winner is not False:
            if winner == 0:
                messagebox.showinfo("Game Over", "It's a draw.")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
        else:
            current_player = PLAYER_ONE if current_player == PLAYER_TWO else PLAYER_TWO
 

def update_board():
    '''
    Update the visual state of the board
    '''
    for row in range(ROWS):
        for col in range(COLUMNS):
            shape = ""
            if board[row][col] == PLAYER_ONE:
                shape = "circle"
            elif board[row][col] == PLAYER_TWO:
                shape = "cross"
            if shape == 'circle':
                #Draw a circle in the appropriate location
                x_0 = col*CANVAS_WIDTH/3
                y_0 = (row)*CANVAS_HEIGHT/3
                x_1 = (col+1)*CANVAS_WIDTH/3
                y_1 = (row+1)*CANVAS_HEIGHT/3
                canvas.create_oval(x_0,y_0,x_1,y_1,outline='black')
            elif shape == 'cross':
                #Draw cross in the appropriate location
                x_0_1 = x_0_2 = col*CANVAS_WIDTH/3
                x_1_1 = x_1_2 = (col+1)*CANVAS_WIDTH/3
                y_0_1 = y_1_2 = row*CANVAS_HEIGHT/3
                y_1_1 = y_0_2 = (row+1)*CANVAS_HEIGHT/3
                canvas.create_line(x_0_1, y_0_1, x_1_1, y_1_1, fill='black')
                canvas.create_line(x_0_2, y_0_2, x_1_2, y_1_2, fill='black')
             
                
def reset_board():
    global board, current_player
    board = [[EMPTY for x in range(COLUMNS)] for y in range(ROWS)]
    canvas.delete('all')
    update_board()
    initialize_board()
    current_player = PLAYER_ONE


def initialize_board() -> None:
    """
    Initializes and draws the game board.
    """
    #Initialize background
    #Draw the tic tac toe lines
    #We draw two vertical lines each 1/3 and 2/3 the distance of the top border.
    canvas.create_line(CANVAS_WIDTH/3, 0, CANVAS_WIDTH/3, CANVAS_HEIGHT, fill='black')
    canvas.create_line(2*CANVAS_WIDTH/3, 0, 2*CANVAS_WIDTH/3, CANVAS_HEIGHT, fill='black')
    #We draw two horizontal lines, each 1/3 and 2/3 the distance along the side border.
    canvas.create_line(0, CANVAS_HEIGHT/3, CANVAS_WIDTH, CANVAS_HEIGHT/3, fill='black')
    canvas.create_line(0, 2*CANVAS_HEIGHT/3, CANVAS_WIDTH, 2*CANVAS_HEIGHT/3, fill='black')
    # Bind mouse click to the canvas
    canvas.bind("<Button-1>", lambda event: draw_piece(event.y//(200), event.x//(200)))


initialize_board()

root.mainloop()
