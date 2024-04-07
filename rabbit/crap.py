#dummy modell

#populáció kihasználtsága
pop = 0.4
#növekedési ráta
r = 3
#iterációk száma
tart = 10000
ido = 0

def rabbit(pop, r, tart, ido):

    for x in range(tart):
        ido += 1
        pop = r*pop*(1-pop)
        print(round(pop, 3))

rabbit(pop, r, tart, ido)