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


def rekursion(n, q):
    if n == 0:  # sobald n == 0 wird wollen wir aufhören
        print("geschafft nach {} rekursionen".format(q))
    else:
        rekursion(n-1, q+1)

# Diese Methode ruft sich selbst wieder auf, .format() fügt der reihe nach variablen in {} ein
# alternativ: print(f"geschafft nach {q} rekursionen"), mit f"" geht das auch einfach so

# Aufgaben:
# 1 Schreibe eine Methode, die eine Liste entgegennimmt und das Produkt aller einträge bildet
# 2 Schreibe eine rekursive Methode, die das Programm zum Absturz bringt (es gibt ein rekursionsmaximum)
# 3 Schreibe die fibonacci Reihe rekursiv als Methode

# Danach kannst du in "DatOps" sehen, wie man Dateien liest & schreibt und in CommandLine.py findest du, wie man
# Python Programme mittels Kommandozeile benutzen kann
# Dann geh zu 2NumPy
