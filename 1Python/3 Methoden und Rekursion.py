# Was sind Methoden?
# Methoden sind Objekte, die aufrufbar sind und dinge tun können, z.B. etwas ausrechnen.


def do_something(some_number):
    some_other_number = some_number * 3
    return some_other_number

# DEFINIERE Methodenname (Variablen die die Methode braucht):
#   CODE
#   RETURN etwas (oder kein return wenn wir nichts zurückgeben)

# Man kann auch Datentypen als "Hinweis" angeben


def do_something_typehint(some_number: float) -> float:
    some_other_number = some_number * 3
    return some_other_number

# bleibt alles gleich ABER variable: DATENTYP gibt den erwarteten Datentyp an (der Benutzer kann aber was anderes
# reinschieben
# -> DATENTYP gibt den erwarteten Rückgabewert an


print(do_something(10))
print(do_something_typehint(10))
# Funktioniert beides gleich, man kann aber auch:
print(do_something(some_number=10))
# geht auch

# Rekursion:


def rekursion(n, recursion_counter):
    if n == 0:  # sobald n == 0 wird wollen wir aufhören
        print("geschafft nach {} rekursionen".format(recursion_counter))
        # alternativ: print(f"geschafft nach {recursion_counter} rekursionen")
    else:
        rekursion(n-1, recursion_counter+1)  # wir führen die Methode nochmal aus, ziehen aber 1 von unserem initialem
        # n ab und zählen den counter hoch um 1
        # bsp: rekursion(1, 0):
        # n != 0 -> wir führen rekursion() mit n= 1-1 und counter= 0 + 1 aus
        # dann n == 0 -> wir schreiben "geschafft nach 1 rekursionen"


rekursion(10, 0)

# Diese Methode ruft sich selbst wieder auf, .format() fügt der reihe nach variablen in {} ein
# alternativ: print(f"geschafft nach {q} rekursionen"), mit f"" geht das auch einfach so

# abschließend: man kann auf "default" Argumente angeben:


def methode(variable: int = 0) -> int:
    # Die Methode "Methode" nimmt einen int entgegen, wird keiner angegeben, dann wird "variable = 0" angenommen
    return variable + 1


print(methode(0))
print(methode())
# und damit sind die ausgaben dieser beiden methodenaufrufe gleich

# Aufgaben:
# 1 Schreibe eine Methode, die eine Liste entgegennimmt und das Produkt aller einträge bildet
    # tipp: for schleife
# 2 Schreibe eine rekursive Methode, die das Programm zum Absturz bringt (es gibt ein rekursionsmaximum)
# 3 Schreibe die fibonacci Reihe rekursiv als Methode
# tipp:
# def rec_fib(depth):
#     if depth > 1:
#         return rec_fib(depth - irgendwas) + rec_fib(depth - irgendwas2)
#     return depth
# danach ab zu 4 Objektorientierte programmierung
