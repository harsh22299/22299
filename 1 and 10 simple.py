output = []
MIDDLE = 4
LOWER = 1
UPPER = 10
while True:
    try:
        #asking number from user
        number = int(input("Guess a number between 1 and 10: "))
        if number < LOWER or number > UPPER:
            print("That number is not between 1 and 10")
        elif number == MIDDLE:
            print("Correct")
            break
            number = []
        else:
           print("Incorrect")
           output.append(number)
    except:
        print("That is an invalid guess")
print("Here are your guesses: ")
for character in output:
    print(character)
print(number)
