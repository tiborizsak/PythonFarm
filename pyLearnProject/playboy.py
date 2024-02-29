import random

guessList = ['heads', 'tails']
guess = ''

while toss == guess:
  guess = guessList.index(input('Gimme guess! : '))
  toss = random.randint(0, 1)

  if toss == guess:
    print('Yaay')
  else:
    print('Agaaaain!')