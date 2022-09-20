# wir beschäftigen uns jetzt mit if, while und for
# wir definieren erst ein paar toy-variablen
zahlA = 10
zahlB = 20

if zahlA > zahlB:
    print(zahlA, ">", zahlB)
# WENN Bedingung:
#   CODE
else:
    print(zahlB, ">=", zahlA)
# ANSONSTEN:
#   CODE

# Viel mehr gibt es hier nicht zu sagen -> wir machen weiter mit der while-Schleife
while zahlA < zahlB:
    print(zahlA, "<", zahlB)
    zahlA = zahlA + 1
# SOLANGE Bedingung (erfüllt):
#   WIEDERHOLE CODE
print(zahlA, ">", zahlB)

# Nun die for-Schleife:
for i in range(100):
    print(i)
# FÜR VARIABLE in GENERATOR/ITERABLE:
#   WIEDERHOLE CODE BIS GENERATOR/ITERABLE am ende
# Was ist ein Generator?:


def generator(q):
    n = -1
    while n < q:
        n += 1
        yield n
# Ein Generator gibt bei jedem Aufruf ein Objekt zurück bis ein bestimmtes Kriterium erreicht wurde
# Hier: solange n kleiner als unser angegebenes q ist, geben wir n zurück und addieren 1 dazu (nennt man inkrementieren)
# "def" erklären wir später


for i in generator(4):
    print(i)
# Wie wir sehen tut es genau das selbe wie range (nur nehmen wir q noch mit könnten aber aus while n < q-> n <= q machen

# Aufgaben:
# 1 Schreibe eine Schleife, die nur gerade Zahlen ausgibt (Tipp: "%" ist ganzzahlteilung)
# 2 Schreibe eine Schleife, die die fibonacci Reihe bis zum 10. Element berechnet (Tipp: du Variablen in & vor einer
#   Schleife erstellen und benutzen
# 3 (optional) schreibe den Generator um, sodass er von q runterzählt bis 0
