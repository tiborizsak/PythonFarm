lista = ['cica', 'kutya', 'elefant', 'varju']

print(lista.index('varju'))

lista.insert(2, 'orangutan')

print(lista)

lista.append('kakkadu')

print(lista)

lista.remove('cica')

print(lista)

del lista[3]

szamoslista = [1, 6, 2, 5, 10, 11]
szamoslista.sort()
print(szamoslista)

lista.sort()
print(lista)

#True alphabetical order
#list.sort(key=str.lower)
#That does not work(?)

# Similar modifications on a string

szoveg = 'Hadesz egy kis pelo'
ujSzoveg = szoveg[0:6] + ' a ' + szoveg[11:]

print(ujSzoveg)

egylista = ['sokinfo', 3.14, 'New York', 12303, 'valamiinfo']

valamiLista = egylista

valamiLista[1] = 100

print(egylista)
print(valamiLista)

import copy

masollista = ['info', 'valaminfo', 'izeinfo']

ujLista = copy.deepcopy(masollista)

print(ujLista)

ujLista.append('Bangladesh')

print(ujLista)
print(masollista)