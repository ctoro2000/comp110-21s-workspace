"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730325562"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune = randint(1, 4)
if fortune == 1:
    print("You find beauty in ordinary things, do not lose this ability.")
else:
    if fortune == 2:
        print("You will be awarded some great honor.")
    else:
        if fortune == 3:
            print("It's not the plan that is important, it's the planning.")
        else: 
            print("You will find an outlet for your creative genius and accomplish a great deal.") 