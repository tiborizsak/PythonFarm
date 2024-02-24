for i in range(0, 10):
    print(i)

szazas = list(range(0,101))

print(szazas)

for z in range(len(szazas)):
    print(z)

# Multiple assignment

kutymek = ['harapos', 'okos', 'fekete']

milyen, okose, milyenszinu = kutymek

print(milyen)
print(okose)
print(milyenszinu)

a = 'CCC'
b = 'ZZZ'

a, b = b, a

print(a, b)

szam = 45
szam += 1