import pprint

hadesz = {'meret': 'kicsi', 'viselkedes': 'kotsog', 'hasznos': 'nem'}

print("A kutyam " + hadesz['meret'])

print('szor' in hadesz)

print(list(hadesz.keys()))
print(list(hadesz.values()))
print(list(hadesz.items()))

for i in hadesz.keys(): #also values and items
    print(i)

for k, v in hadesz.items():
    print(k, v)

print(hadesz.get('szor', 'nincs szor'))

if 'szor' not in hadesz:
    hadesz['szor'] = 'barna'

print(hadesz.get('szor', 'nincs szor'))

hadesz.setdefault('kor', 'oreg')

print(hadesz)

uzenet = 'Valami generelikus lorem ipsum pleszholder szoveg'
count = {}

for c in uzenet:
    count.setdefault(c, 0)
    count[c] = count[c] + 1

print(count)

szamlalo = {}

for c in uzenet.upper():
    szamlalo.setdefault(c, 0)
    szamlalo[c] = szamlalo[c] + 1

print(szamlalo)

pprint.pprint(szamlalo) #pretty print