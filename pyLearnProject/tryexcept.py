#print("Hány fogad van?")

hanyFog = input("Hany fogad van?")
#print(hanyFog)

try:
    if int(hanyFog) == 32:
        print("Pont annyi fogad van mint kell!")
    elif int(hanyFog) < 32 and 20 < int(hanyFog):
        print("Megteszi!")
    else:
        print("Biztos jól tudsz furulyázni, mert semmi fogad nincs!")
except ValueError:
    print("Ne szórakozz már nem is számokat adtál meg!")
