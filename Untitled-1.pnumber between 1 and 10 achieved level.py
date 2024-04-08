"""NCEA Tested Questions, Question 2"""
while True:
    num = int(input("Guess a number from 1 to 10: "))
    if num == 4:
        print('Correct')
        break
    else:
        print("Incorrect")
print("Here are your guesses:")
list(input)