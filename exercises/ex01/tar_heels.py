"""An exercise in remainders and boolean logic."""

__author__ = "730325562"


# Begin your solution here...
val = int(input("Enter an int: "))
if val % 2 == 0:
    if val % 7 == 0:
        print("TAR HEELS")
    else:
        print("TAR")
else:  
    if val % 7 == 0:
        print("HEELS")
    else:
        print("CAROLINA")