"""This program builds a Mad Libs story. Mad Libs require words from the reader for the blank spaces and a story to plug the words into."""

"""Informing the user that the program has started"""
# IDE - Integrated Development Environment (makes your life easier)
print "Hello there, Mad Libs has started!" 

"""The story needs a main character. Asing the user to input a name for the main character"""
protagonist = raw_input("Input a name for the main character in the story:")

"""For the story we will need to ask the user for three adjectives"""
adjective_1 = raw_input("Input adjective 1:")
adjective_2 = raw_input("Input adjective 2:")
adjective_3 = raw_input("Input adjective 3:")

"""We will also need to ask the user for three verbs"""
verb_1 = raw_input("Input verb 1:")
verb_2 = raw_input("Input verb 2:")
verb_3 = raw_input("Input verb 3:")

"""We will now need to ask the user for four nouns"""
noun_1 = raw_input("Input noun 1:")
noun_2 = raw_input("Input noun 2:")
noun_3 = raw_input("Input noun 3:")
noun_4 = raw_input("Input noun 4:")

"""Now we ask the user to input one of each of the following"""
an_Animal = raw_input("Name one animal:")
a_food = raw_input("Name a food:")
a_fruit = raw_input("Name one fruit:")
a_number = raw_input("Name one number:")
a_superhero = raw_input("Give one superhero name:")
a_country = raw_input("Name one country:")
a_dessert = raw_input("Name one dessert:")
a_year = raw_input("Name a year:")

print 'Program execution is starting!'
#The template for the story
story = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (Adjective_1, Protagonist, Verb_1, Adjective_2, Noun_1, Noun_2, An_Animal, A_food, Verb_2, Noun_3, A_fruit, Adjective_3, Protagonist, Verb_3,  A_number, Protagonist,  A_superhero, A_superhero, Protagonist, A_country, Protagonist,  A_dessert, Protagonist, A_year,  Noun_4)

print story
