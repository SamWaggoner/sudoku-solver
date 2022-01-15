# Sudoku solver in Python
# Samuel Waggoner
# Began 1/9/22

def solve(board):


    origBoard = board

    # in board possibilities, open spaces
    boardPossibilities = []
    for i in range(9):
        column = ['x','x','x','x','x','x','x','x','x']
        # column = ['x']
        boardPossibilities.append(column)

    for i in range(1,10):
        for x in range(9):
            for y in range(9):
                if board[x][y] == i:
                    pass
    num = 0
    origBoard[x][y] = num
    return(solve(origBoard))


def printBoard(board):

    # check to make sure board is valid
    if len(board) != 9:
        print("Incorrect board: number columns incorrect")
    for i in range(9):
        if len(board[i]) != 9:
            print("Incorrect board: Column " + str(i))

    print("-------------------------------------")
    for k in range(3):
        if k == 0 or k == 2:
            pass
        for i in range(3*k,3*k+3):
            row = []
            for j in range(9):
                row.append(" ")
                row.append(board[j][i])
            del row[0]
            row.insert(0,'|')
            row[6] = '|'
            row[12] = '|'
            row.append('|')
            row = str(row)
            row = row.replace('[','')
            row = row.replace(']','')
            row = row.replace('\'','')
            row = row.replace(',','')
            print(row)
    print("-------------------------------------")

    # create numbers in right arrangement, creating them by row as a list,
    # inserting lines, and then printing the row as a string, removing list visuals
    print("-------------------------------------")
    for i in range(0,3):
        row = []
        for j in range(9):
            row.append(" ")
            row.append(board[j][i])
        del row[0]
        row.insert(0,'|')
        row[6] = '|'
        row[12] = '|'
        row.append('|')
        row = str(row)
        row = row.replace('[','')
        row = row.replace(']','')
        row = row.replace('\'','')
        row = row.replace(',','')
        print(row)
    print("|-----------------------------------|")
    for i in range(3,6):
        row = []
        for j in range(9):
            row.append(" ")
            row.append(board[j][i])
        del row[0]
        row.insert(0,'|')
        row[6] = '|'
        row[12] = '|'
        row.append('|')
        row = str(row)
        row = row.replace('[','')
        row = row.replace(']','')
        row = row.replace('\'','')
        row = row.replace(',','')
        print(row)
    print("|-----------------------------------|")
    for i in range(6,9):
        row = []
        for j in range(9):
            row.append(" ")
            row.append(board[j][i])
        del row[0]
        row.insert(0,'|')
        row[6] = '|'
        row[12] = '|'
        row.append('|')
        row = str(row)
        row = row.replace('[','')
        row = row.replace(']','')
        row = row.replace('\'','')
        row = row.replace(',','')
        print(row)
    print("-------------------------------------")
            

def main():
    board = []
    for i in range(9):
        column = ['x','x','x','x','x','x','x','x','x']
        board.append(column)
    board[0][0] = '3'
    board[4][1] = '3'
    board[8][4] = '3'
    board[7][3] = '3'
    printBoard(board)

main()