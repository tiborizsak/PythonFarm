lista = [1, 2, 3, 7, 'kiskutya']

#print(type(lista[0]))
print(type(lista[-1]))

listaAlistaban =  [['valami', 'valamimas'], 323, 5234, 6456]

print(type(listaAlistaban[0]))
print(type(listaAlistaban[1]))

listahozzadas = [1, 2, 3, 4, 7]
listahozzadas[2] = 'lofasz'
listahozzadas[3:4] = ['asztal', 'szek']

print(listahozzadas)

listaListazas = ['izeke', 'mizeke', 'valami', 'semmike']

print(listaListazas[:2])
print(listaListazas[1:])

listaElemTorles = ['izeke', 'mizeke', 'valami', 'semmike']
del listaElemTorles[:3]

print(listaElemTorles)

'semmike' in listaElemTorles # True