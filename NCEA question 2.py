"""NCEA Question 2, Harsh Gautam"""
output = []
MIDDLE = 4
LOWEST = 1
HIGHEST = 10
while True:
    try:
        #asking number from user.
        number = int(input("Guess a number from 1 to 10:  "))
        #code that determines whether number is within 1 and 10, if not program will print "That number is not between 1 and 10".
        if number < LOWEST or number > HIGHEST:
            print("That is not between 1 and 10.")
        #code that prints "correct" if user gives answer 4 or incorrect if any other number between 1 and 10 is given.
        elif number == MIDDLE:
            print("Correct.")
            break
            number = []
        else:
           print("Incorrect.")
           output.append(number)
    except:
        print("That is an invalid guess.")
#listing the users guesses
print("Here are your guesses: ")
for character in output:
    print(character)
print(number)