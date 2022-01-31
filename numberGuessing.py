import random
chances = 0
randomnumber = random.randint(1,9)
print("Number Guessing Game!!")
print("Guess a number between 1 & 9")

while chances < 5 :

        yourguess = int(input("Your guess: "))

        if randomnumber == yourguess:
            print("You won!!")
            break

        elif yourguess < randomnumber:
            print("Your guess is low. Guess a number greater than ", yourguess)

        else:
            print("Your guess is high. Guess a number lesser than ",yourguess)

            chances += 1

if not chances < 5:
    print("You lost!! the number is", randomnumber)
