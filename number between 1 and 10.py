while True:
    num = int(input("Guess a number from 1 to 10: "))
    if num < 0:
        print("That is not between 1 and 10.")
    elif num > 10:
        print("That is not between 1 and 10.")
    elif num == 4:
        print('Correct')
