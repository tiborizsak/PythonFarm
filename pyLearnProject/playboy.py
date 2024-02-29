import random

guessList = ['heads', 'tails']
guess = ''
toss = ''

while toss == guess:
  guess = guessList.index(input('Gimme guess! : '))
  toss = random.randint(0, 1)

  if toss == guess:
    print('Yaay')
  else:
    print('Agaaaain!')

def guessTheNumber(numberofrounds, finite)
  if numberofrounds > 0:
    for i in range(numberofrounds + 1):
      toss = random.randint(0, 1)
      guess = guessList.index(input('Gimme guess! : '))
      if toss == guess:
        print('yaaaaaay')
      else:
        print()

def guessthenumma():
  toss = random.randint(0, 1)
  guess = guessList.index(input('Gimme output! : '))
  return toss == guess