"""In this project, I build a program that rolls a pair of dice and asks the user to guess a number. Based on the user's guess, the program should determine a winner. If the user's guess is greater than the total value of the dice roll, they win! Otherwise, the computer wins. The program should do the following: 1. Randomly roll a pair of dice. 2. Add the values of the roll. 3. Ask the user to guess a number. 4. Compare the user's guess to the total value. 5. Decide a winner (the user or the program). 6. Inform the user who the winner is"""

"""Since the program will roll a dice, we need to make sure the roll are random. To do so, I will need some Python code that isn't built-in or readily available to us. Thankfully, I can import the module that will help me. """
from random import randint

"""I will also need to import more Python code that will be used to simulate dice rolling."""
from time import sleep

"""Now I will need to prompt the user for their guess"""
def get_user_guess():
    user_guess = int(raw_input("Guess a number: "))
    return user_guess
 
"""Now we build the rest of the game. The roll_dice function will be used to simulate the rolling of a pair of dice."""
def roll_dice(number_of_sides):
    number_of_sides = int(raw_input("Specify the number of sides a single dice will have: "))
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print " %i is the maximum possible value from the sum of the two dice " % max_val
    sleep(1)
    user_guess = get_user_guess()
    if user_guess > max_val:
        print "No guessing higher than the maximum possible value!"
        return
    else:
        print "Rolling..."
        sleep(2) 
        print "%d" % first_roll
        sleep(1)
        print "%d" % second_roll
        sleep(1)
        total_roll = first_roll + second_roll
        print "%d" % total_roll
        print "Result..."
        sleep(1)
        if user_guess > total_roll:
            print "Congratulations!!! You won!!!"
            return
        else:
            print "May God fill your heart with strength to bear the shame! Because you just lost the game!!!."
            return
          
roll_dice(6)
      
  
