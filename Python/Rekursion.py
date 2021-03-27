# wir basteln eine methode die sich selbst aufruft, bis ein ereignis eingetreten ist
def rekursion(n, q):
    if n < 0:
        print("geschafft nach {} rekursionen".format(q))
    else:
        rekursion(n-1, q+1)


if __name__ == "__main__":
    rekursion(200, 0)


#Vorteile: Was für Vorteile? Man braucht die manchmal einfach z.B. in rekurrenten neuronalen netzen
#Nachteile: alles was wir bis zur n. rekursion gemacht haben muss auch rückwärts nachgerechnet werden damit die methode abgeschlossen ist
#Außerdem haben wir ein rekursionslimit