
board = ['-','-','-','-','-','-','-','-','-']



def print_board(board):
    print board[0:3]
    print board [3:6]
    print board [6:9]

def play_game(board, mover, move):
    moveIndex = None
    if move == "top left":
        moveIndex = 0 
    elif move == "top middle":
        moveIndex = 1 
    elif move == "top right":
        moveIndex = 2 
    elif move == "middle left":
        moveIndex = 3 
    elif move == "middle middle":
        moveIndex = 4 
    elif move == "middle right":
        moveIndex = 5 
    elif move == "bottom left":
        moveIndex = 6 
    elif move == "bottom middle":
        moveIndex = 7 
    elif move == "bottom right":
        moveIndex = 8
    if moveIndex == None:
        return False
    if board[moveIndex] != "-":
        return False
    else: 
        board[moveIndex] = mover
        return True

listOfMoves = ['top left', 'top middle', 'top right', 'middle left', 'middle middle', 'middle right', 'bottom left', 'bottom middle', 'bottom right']

def calling_list_of_moves(listOfMoves):
    spotNumber = 0 + 1
    return listOfMoves.pop(spotNumber)

testingBoard =['-','-','-','-','-','-','-','-','-']

boardSpace = testingBoard[0]
def testing_board(testingBoard, boardSpace):
    testingMove = 'X'
    blankSpace = '-'
    boardSpace = 0 
    newSpace = boardSpace + 1 
    testingBoard.insert(newSpace, testingMove)
    return testingBoard

    

def game_eval(board):
    if board[0] == "X" and board[1] == "X" and board[2]== "X":
        return True
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        return True   
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        return True 
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return True 
    elif board[2] == "X" and board[5] =="X" and board[8] == "X":
        return True
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        return True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        return True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        return True
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        return True
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        return True
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        return True 
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        return True 
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return True 
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return True
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        return True
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        return True
    else:
        return False









if __name__ == "__main__":
    # set up anything you need 

    print testing_board(testingBoard, boardSpace)
    print testing_board(testingBoard, boardSpace)

#who wins and how to do typos

    mover = "X"
    moves = 0
    while game_eval(board) == False:
        print_board(board)
        print " What is your move?"
        move = raw_input()
        validMove = play_game(board, mover, move)
        if validMove == True:
            moves = moves + 1
            if mover == "X":
                mover = "O"
            elif mover == "O":
                mover = "X"
        else: 
            print "invalid move try again"       
    print_board(board)
    print "game over"
