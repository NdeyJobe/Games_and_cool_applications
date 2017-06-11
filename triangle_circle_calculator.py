"""This project creates a calculator that can compute the area of a given shape, as selected by the user"""

"""Since we will calculate the area of a circle, we will need to import the value pi"""
from math import pi

"""We will also need access to some more Python code that will be used to simulate a thinking calculator"""
from time import sleep

"""When the program starts, we will print the date and time for the user so we will also need to import date and time"""
from datetime import datetime

"""Now we need to retrieve the current date and time"""
now = datetime.now()

"""Printing a message to the user to know that the calculator is starting up"""
print "Calculator is starting up..."

"""Printing out the current month, day, year, hour, and minute (in that order)"""
print "%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)

"""Now we ask the program to sleep for 1 second. To sleep a program means to delay it from processing the next line of code by an amount of time that you specify"""
sleep(1)

"""Including the correct units"""
hint = "Don't forget to include the correct units! \nExiting..."

"""To find out what shape to calculate the area of"""
option = raw_input("What shape do you want to calculate the area of? Enter C for Circle or T for Triangle:")

"""Making sure that the user response is upper case"""
option = option.upper()

"""Time to calculate the area of the shape the user specifies. We wrap the raw_input with float(), as this will make sure we are storing the user's input as a floating point number. %.2f. gives area answer in two decimal places and \n prints Hint on next line.
"""
if option == "C":
    radius = float(raw_input("Enter radius:"))
    area = pi * (radius ** 2)
    print "The pie is baking..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
elif option == "T":
    base = float(raw_input("Enter the base of the triangle:"))
    height = float(raw_input("Enter the height of the triangle:"))
    area = 1.0/2 * base * height
    print "Uni Bi Tri..."
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
else:
    print "garbage entered, program will exit!"


    
