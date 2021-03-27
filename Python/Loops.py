#der while Loop:
q = 25
while q > 0:#solange die bedingung gilt:
    print(q)#schreibe q in die kommandozeile
    q -= 1#und subtrahiere dann 1 von q

#die for-schleife:
for _ in range(25):#beliebes generatorobjekt oder liste/array... alles was verkettet ist
    print(_)

beispielliste = ["Ein", "kleines", "Haus", "steht", "auf", "dem", "Berg"]
for _ in beispielliste:
    print(_)
#Wir iterieren mit einem pointer (hier _) über die liste und geben jedes zum pointer gehörende element aus

#do-while:
q = 25
while True:
    print(q)
    q -= 1
    if q < 0:
        break
#Wir checken nach ausführung ob die bedingung noch erfüllt ist
#EXKURSTIMEEEEE