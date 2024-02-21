
def someAwesomeFunction (a,b):
    if a != "Homer Simpson" and b != "Bart Simpson":
        print("Your guess sucks!")
    elif a != "Homer Simpson" and b == "Bart Simpson":
        print("Well! It is still not Homer Simpson, but at least Bart Simpson")
    else:
        print("YOU TOTALLY NAILED IT!!")
    
def doOtherStuff ():
   a = input("Guess a character from The Simpsons: ")
   b = input("Guess another character: ")
   someAwesomeFunction(a,b)

