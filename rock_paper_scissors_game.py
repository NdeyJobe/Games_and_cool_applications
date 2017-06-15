"""In this project, I'll build Rock-Paper-Scissors! The program should do the following: 1.Prompt the user to select either Rock, Paper, or Scissors. 2.Instruct the computer to randomly select either Rock, Paper, or Scissors. 3. Compare the user's choice and the computer's choice. 4. Determine a winner (the user or the computer). 5.Inform the user who the winner is"""

"""The game will require python codes that are not built in so I import the modules random and time."""
from random import randint
from time import sleep

OPTIONS = ["R", "P", "S"]
LOST_RESULT = "You Lost"
WIN_RESULT = "You Won"

"""Since the user must select an option and the computer must also select an option, I need a way to decide who the winner is. 
So I add the function decide_winner"""
def decide_winner(user_choice, computer_choice):
    print "%s" % str(user_choice)
    print "Computer selecting..."
    sleep(1)
    print "%s" % str(computer_choice)
    user_choice_index = OPTIONS.index(user_choice)
    computer_choice_index = OPTIONS.index(computer_choice)#Now I code the rules that will determine the winner
    if user_choice == computer_choice:
        print "Dude, its a tie!"
    elif user_choice_index == 0 and computer_choice_index == 2:
        print "Congratulations!!! You have won!"
    elif user_choice_index == 1 and computer_choice_index == 0:
        print "Congratulations!!! You have won!"
    elif user_choice_index == 2 and computer_choice_index == 1:
        print "Congratulations!!! You have won!"
    elif user_choice_index > 2:
        print "An invalid option was selected!"
        return
    else:
        print "You Lost! Better luck next time. "
        
"""Now that I have a function that will decide who the winner is, I will write a function that will actually start the game"""
def play_RPS():
    print "Welcome! You are about to begin the game Rock-Paper-Scissors"
    user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
    sleep(1)
    user_choice = user_choice.upper()
    computer_choice = OPTIONS[randint(0, len(OPTIONS)-1)]
    decide_winner(user_choice, computer_choice)
    
play_RPS()
  
   
