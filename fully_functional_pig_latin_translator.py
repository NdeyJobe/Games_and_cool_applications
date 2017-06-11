#Code for a fully functional PIG latin Translator

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
    

