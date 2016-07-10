from random import randint
from termcolor import colored, cprint
board=[]
toprow=[
colored('*','grey','on_cyan'),
colored('1','grey','on_cyan'),
colored('2','grey','on_cyan'),
colored('3','grey','on_cyan'),
colored('4','grey','on_cyan'),
colored('5','grey','on_cyan')]
board.append(toprow)
leftcol=[
colored('A','grey','on_cyan'),
colored('B','grey','on_cyan'),
colored('C','grey','on_cyan'),
colored('D','grey','on_cyan'),
colored('E','grey','on_cyan')]
for x in range(5):
    row=[colored('O','white','on_blue')] * 5
    row.insert(0,leftcol[x])    
    board.append(row)
def print_board(board):
    for printrow in board:
        if printrow==toprow:
            print colored(' ','grey','on_cyan').join(printrow)
        else:
            print colored(' ','grey','on_blue').join(printrow)
title1=colored("Let's play ",'yellow','on_grey')
title2=colored('Battleship!','red','on_grey')
print title1+title2
print ''
cprint('You get four chances!','yellow','on_grey')
cprint('Turn 1:','red','on_grey')
print_board(board)
def random_row(board):
    return randint(1, len(board) - 1)
def random_col(board):
    return randint(1, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
for turn in range(4):
    guess_row_letter=raw_input(colored('Guess Row:','yellow','on_grey'))
    guess_col=int(raw_input(colored('Guess Col:','yellow','on_grey')))
    if guess_row_letter=='A' or guess_row_letter=='a':
        guess_row=1
    elif guess_row_letter=='B' or guess_row_letter=='b':
        guess_row=2
    elif guess_row_letter=='C' or guess_row_letter=='c':
        guess_row=3
    elif guess_row_letter=='D' or guess_row_letter=='d':
        guess_row=4
    elif guess_row_letter=='E' or guess_row_letter=='e':
        guess_row=5
    else:
        guess_row=0
    if guess_row == ship_row and guess_col == ship_col:
        cprint('Congratulations! You sunk my battleship!','yellow','on_grey')
        break
    else:
        if guess_row==0 or (guess_col < 1 or guess_col > 5):
            cprint("Oops, you didn't even hit the ocean!",'yellow','on_grey')
            if guess_row==0:
                cprint('Make sure to put a letter for the row!','yellow','on_grey') 
        elif(board[guess_row][guess_col]==colored('X','red','on_blue')):
            cprint('You guessed that space already!','yellow','on_grey')
        else:
            cprint('You missed my battleship!','yellow','on_grey')
            board[guess_row][guess_col] = colored('X','red','on_blue')
        if turn==3:
            cprint('Game over! Better luck next time!','yellow','on_grey')
            break		
    	
    turnnum=colored(str(turn+2),'red','on_grey')
    print ''
    print colored('Turn ','red','on_grey')+turnnum+':'
    print_board(board)
