#TicTacToe
from IPython.display import clear_output

def myboard(board):
    print ("___"*2)
    print ("|"+board[1]+"|"+board[2]+"|"+board[3]+"|")
    print ("---"*2)
    print ("|"+board[4]+"|"+board[5]+"|"+board[6]+"|")
    print ("---"*2)
    print ("|"+board[7]+"|"+board[8]+"|"+board[9]+"|")
    print ("---"*2)


print ("Welcome to TIC TAC TOE")
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
count = 0
def player_input():
    mark = input("Choose between 'X' or 'O' : ")
    pos = input("Enter the position : ")
    space_check(board, mark, pos)

def place_marker(board, marker, position):
    board[int(position)] = marker
    count += 1
    myboard(board)
    win_check(board,marker)

def win_check(board,mark):
    if ((board[1] == mark) & (board[2] == mark) & (board[3] == mark)) | ((board[4] == mark) & (board[5] == mark) & (board[6] == mark)) | ((board[7] == mark) & (board[8] == mark) & (board[9] == mark)) | ((board[1] == mark) & (board[4] == mark) & (board[7] == mark)) | ((board[2] == mark) & (board[5] == mark) & (board[8] == mark)) | ((board[3] == mark) & (board[6] == mark) & (board[9] == mark)) | ((board[1] == mark) & (board[5] == mark) & (board[9] == mark)) | ((board[3] == mark) & (board[5] == mark) & (board[7] == mark)):
        print ('Congratulations!!! '+ mark +' won the game')
        print ('--'*20)
        again = input('Do you want to play again? Press y/n')
        if again == 'y':
            replay()
        else:
            print('Have a good day')
    else:
        player_input()

def space_check(board, mark, position):
    if board[int(position)] == ' ':
        place_marker(board, mark, position)
    else:
        print ('Pls enter a position that is empty')
        player_input()

def full_board_check(board, mark):
    if ((board[1] == ' ') | (board[2] == ' ') | (board[3] == ' ') | (board[4] == ' ') |(board[5] == ' ') | (board[6] == ' ') |   (board[7] == ' ') |(board[8] == ' ') | (board[9] == ' ')):
        win_check(board, mark)
    else:
        print ("That's a draw")
        print ('--'*10)
        again = input('Do you want to play again? Press y/n')
        if again == 'y':
            replay()
        else:
            print('Have a good day')

def replay():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_input()

player_input()

