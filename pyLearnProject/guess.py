# Guess the number from 5 tries

import random

neve = input('Tell me your name! ')
print('Hi ' + neve + ' ! I am thinking of a number! Find it out bitch!')
titkosNamber = random.randint(1, 20)

for gt in range(1,6):
    guess = input('Gimme guess! ')
    triesleft = 6 - gt

    if int(guess) == titkosNamber:
        print("You guessed in " + gt + " tries!")
    elif int(guess) < titkosNamber:
        print("Nah too low! You still have " + str(triesleft) + " tries!")
    elif int(guess) > titkosNamber:
        print("Nah too high! You still have " + str(triesleft) + " tries!")
    else:
        break
        print("You fucked up!")