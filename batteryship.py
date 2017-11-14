"""In this project I will build a simplified, one-player version of the classic board game Battleship! 
In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. 
The player will have 10 guesses to try to sink the ship."""

from random import randint
from time import sleep


board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Welcome to the Northvolt battery ship!!!"   
sleep(2)
print "We are transporting our battery packs to the Atlas Copco mines."
sleep(3)
print "For security reasons we are transporting real packs together with fake ones."
sleep(3)
print "The packs are arranged in rows and columns as shown below: "
sleep(2)
print_board(board)
sleep(1)
print "We challenge you to locate a real pack amongst the 25 packs and we will reward you with a muffin..."
sleep(3)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

for turn in range(4):
    guess_row = int(raw_input("Guess row of real pack:"))
    guess_col = int(raw_input("Guess column of real pack:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You found a real pack! If you are already one of us you deserve a promotion. If you are not, please check our career page at http://northvolt.com/career. You definately belong with us."
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col \
        < 0 or guess_col > 4):
            print "Oops, that pack is not even in our ship."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed!!! This is Northvolt security you tried to mess with."
            sleep(2)
            print "Try hacking again..."
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "We gave you four chances, we missed them all. Go take a nap, and next time dont mess with Northvolt security!"
            break
    print "That was turn:"
    print turn
    sleep(3)
    print "The correct location of a real pack was"
    print_board(board)
    sleep(2)
    print "We are giving you another chance to locate a real pack. This is turn:"
    print (turn + 1)
