csjegyek1 = ['rák', 'oroszlán', 'bak', 'szűz']
csjegyek2 = ['vízöntő', 'nyilas', 'mérleg', 'halak']

korosztaly1 = [20, 30]
korosztaly2 = [31, 50]

def jovendomondo():
    jegy = input('Add meg a csillagjegyed!: ')

    if jegy not in csjegyek1 and jegy not in csjegyek2:
        raise Exception('A megadott csillagjegy nem létezik!')

    kor = input('Add meg a korodat!: ')

    if int(kor) not in range(korosztaly1[0], korosztaly1[-1]) and kor not in range(korosztaly2[0], korosztaly2[-1]):
        raise Exception('A megadott kor nincs benne az elérhető tartományokba!')

    for e in csjegyek1:
        if e == jegy and int(kor) < korosztaly1[-1]:
            print('Szerencséd leszel! Megnyered a a főnyereményt. Pinák, Pénz, és Kocsik!')
        else:
            print("Baszhatod! Szerencsétlen leszel!")

# jovendomondo()

try:
    jovendomondo()
except Exception as hiba:
    print("Ez a hiba merült fel: " + str(hiba))

# print('nyilas' in csjegyek1 or 'nyilas' in csjegyek2)
# print(10 not in range(korosztaly1[0], korosztaly1[-1]))

# ASSERTION: assert basic sanity check
# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# ages [73, 47, 80, 17, 15, 22, 54, 92, 57, 26]
# assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.