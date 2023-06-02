# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# This is a welcoming print-statement. 
print("Welcome to the crazy cat persona-quiz!")

# This asks the user if they want to continue.
quizing = input("Do you want to play, yes or no? ")

# If the user answer is yes, the quiz begins, if no, it quits.
if quizing != "yes":
    quit()

# If the user answer was yes, the first question is printed.
print("OK! Let's see how much you know about cats! First question:")

# The user has to print the letter or the answer to get it right.
question1 = input("What is a cat? a) predator b) perpetrator ")
if question1 != "a" or "predator":
    print("Wrong!")  
else:
    print("Right!")

# All the other questions that follows, prints and if/else 
# statements is a repitition of the first one.
question2 = input("Which sounds comes from a cat? a) mjao b) quack ")
if question2 == "a" or "mjao":
    print("Right!")

else: 
    print("Wrong! Right answer was: a) mjao")

question3 = input("What is a Singapura? a) country b) cat ")
if question1 == "b" or "cat":
    print("Right!")

else: 
    print("Wrong! Right answer was: b) cat")

question4 = input("Which are the cutest? a) kittens b) puppies ")
if question1 == "a" or "kittens":
    print("Right!")

else: 
    print("Wrong! Right answer was: a) kittens")

question5 = input("Which month is most related to cats? a) may b) march ")
if question1 == "b" or "march":
    print("Right!")

else:     
    print("Wrong! Right answer was: b) march")

print("You have finished the quiz. Your score was -- ")
