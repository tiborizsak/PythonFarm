import random

guessList = ['heads', 'tails']

# def guessthenumma(numberofrounds, finite):
#   toss = random.randint(0, 1)
#   print(toss)
#   guess = guessList.index(input('Gimme output! : '))
#   numrounds = numberofrounds
#   print(numrounds)
#
#   while numrounds != 0:
#     print(numrounds)
#     if toss == guess:
#       print('Yaaay! Exiting...........')
#       numrounds = 0
#     else:
#       if finite == True:
#         numrounds = numberofrounds - 1
#         guessthenumma(numrounds, True)
#       else:
#         print('You suck in this game')
#         numrounds = numberofrounds + 1
#         guessthenumma(numrounds, False)
#
# guessthenumma(5, True)

def gueessthenummer(numberofrounds):
  for i in range(int(numberofrounds)):
    toss = 0
    guess = 1

    if toss != guess:
      guess = guessList.index(input('Gimme a guess heads or tails! : '))
      toss = random.randint(0, 1)
      print('You suck! New round!')
    else:
      print('You missed it!')
      numberofrounds = 0

gueessthenummer(5)

import random

def coin_toss_game(rounds=1, finite=True):
    valid_choices = ["heads", "tails"]
    wins = 0

    for round_number in range(1, rounds + 1) if finite else iter(int, 1):
        user_guess = input("Guess 'heads' or 'tails': ").lower()
        while user_guess not in valid_choices:
            print("Invalid choice. Please choose 'heads' or 'tails'.")
            user_guess = input("Guess 'heads' or 'tails': ").lower()

        toss_result = random.choice(valid_choices)
        print(f"Round {round_number}: The coin toss result is {toss_result}.")

        if user_guess == toss_result:
            wins += 1
            print(f"You guessed correctly! Total wins: {wins}\n")
            if not finite:
                continue
            else:
                break
        else:
            print("You guessed wrong. Try again!\n")
            if not finite:
                continue

    print(f"Game over. You won {wins} time(s).")

# Example usage:
rounds = int(input("Enter the number of rounds: "))
finite_input = input("Should the game end after a specific number of rounds? (yes/no): ").lower()
finite = finite_input == "yes"

coin_toss_game(rounds, finite)
