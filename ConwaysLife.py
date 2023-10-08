import time

def display_board(board_input: list) -> None:
    for row in board_input:
        print(''.join(row))
    print("\n")

def unpack_board(board_input: list) -> list:
    #Convert the list of strings into a list of separated dots, for easier processing
    board_list = []
    for elem in board_input:
        board_list.append([*elem])
    return board_list

def isAlive(cell: str) -> bool:
    return cell == '*'

def neighbor_counts(board_input: list) -> list:
    counts = []
    rows = len(board_input)
    columns = len(board_input[0])
    for i in range(rows):
        row = []
        for j in range(columns):
            #Top left case
            if i == 0 and j == 0:
                count = 0
                neighbors = [(i+1, j), (i, j+1), (i+1, j+1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
            #Bottom left case:
            elif i == rows-1 and j == 0:
                count = 0
                neighbors = [(i-1, j), (i-1, j+1), (i, j+1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
            #Bottom right case:
            elif i == rows-1 and j == columns-1:
                count = 0
                neighbors = [(i-1, j), (i-1, j-1), (i, j-1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
            #Top right case
            elif i == 0 and j == columns-1:
                count = 0
                neighbors = [(i+1, j), (i+1, j-1), (i, j-1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
            #Left edge case
            elif j == 0:
                count = 0
                neighbors = [(i-1, j), (i+1, j), (i, j+1), (i-1, j+1), (i+1, j+1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
            #Right edge case
            elif j == columns-1:
                count = 0
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i-1, j-1), (i+1, j-1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
            #Top edge case
            elif i == 0:
                count = 0
                neighbors = [(i, j+1), (i, j-1), (i+1, j), (i+1, j-1), (i+1, j+1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
            #Bottom edge case
            elif i == rows-1:
                count = 0
                neighbors = [(i, j+1), (i, j-1), (i-1, j), (i-1, j-1), (i-1, j+1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
            #All other cases
            else:
                count = 0
                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]
                for elem in neighbors:
                    if isAlive(board_input[elem[0]][elem[1]]):
                        count += 1
                row.append(count)
        #Add all counts to each list row, which will then be added as a 2d list.
        counts.append(row)
    return counts

def next_gen(board_input: list) -> list:
    board_neighbors = neighbor_counts(board_input)
    rows = len(board_input)
    columns = len(board_input[0])

    #Loop through the board, and see if they should be alive or dead in the next generation.
    for i in range(rows):
        for j in range(columns):
            #Check alive cells
            if isAlive(board_input[i][j]):
                if board_neighbors[i][j] < 2 or board_neighbors[i][j] > 3:
                    board_input[i][j] = "."
            else:
                if board_neighbors[i][j] == 3:
                    board_input[i][j] = "*"
    return board_input

def main():
    
    board =[
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '.....................................................................................*..............................................................................',
        '...................................................................................*.*..............................................................................',
        '.........................................................................**......**............**...................................................................',
        '........................................................................*...*....**............**...................................................................',
        '.............................................................**........*.....*...**.................................................................................',
        '.............................................................**........*...*.**....*.*..............................................................................',
        '.......................................................................*.....*.......*..............................................................................',
        '........................................................................*...*.......................................................................................',
        '.........................................................................**.........................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',
        '....................................................................................................................................................................',

    ]
    '''
    board =[
        '....',
        '.*..',
        '.*..',
        '....',   
    ]
    '''
    board = unpack_board(board)
    display_board(board)
    i = 1
    while True:
        print(f"Generation {i}")
        board = next_gen(board)
        display_board(board)
        time.sleep(0.05)
        i += 1

    board = next_gen(board)
    display_board(board)
    


    


main()

