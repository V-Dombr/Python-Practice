from random import randint

board = []

for i in range(0, 5):
    board.append(5 * ["O"])

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

print "Row is: %s" % (ship_row)
print "Col is: %s" % (ship_col)

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

if guess_row == ship_row and guess_col == ship_col:
    print "You did it!"
else:
    print "You missed!"