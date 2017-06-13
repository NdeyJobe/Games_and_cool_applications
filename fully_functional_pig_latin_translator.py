"""Code for a fully functional PIG latin Translator Now I will write a python code for a Pig Latin translator. 
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." 
So "Python" becomes "ythonpay." To write a Pig Latin translator in Python, here are the steps we'll need to take: 1.Ask the user to 
input a word in English. 2.Make sure the user entered a valid word. 3.Convert the word from English to Pig Latin. 4.Display the
translation result."""


original = raw_input('Enter a word:') #To ask user for word

if len(original) > 0 and original.isalpha():
    pyg = 'ay'#To add at the end of the word
    word = original.lower() #Make lower case
    first = word[0] #Pick the first letter
    new_word = word + first + pyg #This concatenates from 0
    new_word = new_word[1:len(new_word)] #Concatenates idly
    print word and  new_word
else:
    print 'empty'
    

