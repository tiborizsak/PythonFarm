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
     

def guessthenumma(numberofrounds, finite):
  toss = random.randint(0, 1)
  guess = guessList.index(input('Gimme output! : '))

  while numberofrounds != 0:
  
    if toss == guess:
      print('Yaaay! Exiting...........')
    else:
      if finite == True:
        guessthenumma()
        numberofrounds--
      else:
        print('You suck in this game')
        guesthenumma()
